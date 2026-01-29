# backend.py

import logging
from abc import ABC, abstractmethod
from typing import List, Optional

logger = logging.getLogger(__name__)

# ===============================
# Backend abstract base class
# ===============================

class Backend(ABC):
    """
    Abstract backend interface.
    """

    @abstractmethod
    def generate_batch(self, prompts: List[str], **gen_kwargs) -> List[str]:
        raise NotImplementedError


# ===============================
# Local vLLM backend
# ===============================

class LocalBackend(Backend):
    """
    Local vLLM backend (token-level, batch inference).
    """

    def __init__(
        self,
        model_path: str,
        dtype: str = "auto",
        trust_remote_code: bool = False,
        tensor_parallel_size: int = 1,
        gpu_memory_utilization: float = 0.98,
        max_length: int = 2048,
        stop_words: Optional[list[str]] = None,
    ):
        from transformers import AutoTokenizer
        from vllm import LLM

        logger.info(
            "Initializing LocalBackend | model=%s | dtype=%s | tp=%d | max_length=%d",
            model_path,
            dtype,
            tensor_parallel_size,
            max_length,
        )

        self.model = LLM(
            model=model_path,
            dtype=dtype,
            trust_remote_code=trust_remote_code,
            tensor_parallel_size=tensor_parallel_size,
            gpu_memory_utilization=gpu_memory_utilization,
        )

        self.tokenizer = AutoTokenizer.from_pretrained(
            model_path,
            trust_remote_code=trust_remote_code,
            truncation_side="left",
            padding_side="right",
        )

        if not self.tokenizer.eos_token:
            logger.warning("Tokenizer has no eos_token, using bos_token instead")
            self.tokenizer.eos_token = self.tokenizer.bos_token
        self.tokenizer.pad_token = self.tokenizer.eos_token

        self.max_length = max_length
        self.stop_words = stop_words or ["[/ANSWER]"]

        logger.info("LocalBackend initialized successfully")

    def generate_batch(self, prompts: List[str], **gen_kwargs) -> List[str]:
        from vllm import SamplingParams
        import time

        batch_size = len(prompts)
        logger.debug("LocalBackend.generate_batch | batch_size=%d", batch_size)

        enc = self.tokenizer(
            prompts,
            truncation=True,
            max_length=self.max_length,
            padding=False,
        )

        input_ids = enc["input_ids"]   # List[List[int]]
        input_lens = [len(ids) for ids in input_ids]

        max_new_tokens = int(gen_kwargs.get("max_new_tokens", 128))
        max_tokens = min(
            max_new_tokens,
            min(self.max_length - l for l in input_lens),
        )

        if max_tokens <= 0:
            logger.warning(
                "All prompts too long, skip generation | batch_size=%d", batch_size
            )
            return [""] * batch_size

        sampling_params = SamplingParams(
            temperature=float(gen_kwargs.get("temperature", 0.0)),
            top_p=float(gen_kwargs.get("top_p", 1.0)),
            max_tokens=max_tokens,
            stop=self.stop_words,
        )

        t0 = time.time()
        outputs = self.model.generate(
            prompt_token_ids=input_ids,
            sampling_params=sampling_params,
            use_tqdm=False,
        )
        dt = time.time() - t0

        logger.info(
            "LocalBackend.generate_batch done | batch_size=%d | max_tokens=%d | time=%.2fs",
            batch_size,
            max_tokens,
            dt,
        )

        return [o.outputs[0].text.strip() for o in outputs]


# ===============================
# API backend
# ===============================

class APIBackend(Backend):
    """
    OpenAI / OpenAI-compatible API backend.
    """

    def __init__(
        self,
        base_url: str,
        model: str,
        api_key: Optional[str] = None,
        timeout_s: float = 120.0,
        enable_thinking: bool = False,
    ):
        from openai import OpenAI

        logger.info(
            "Initializing APIBackend | model=%s | base_url=%s",
            model,
            base_url,
        )

        self.client = OpenAI(
            base_url=base_url,
            api_key=api_key,
            timeout=timeout_s,
        )
        self.model = model

        self.enable_thinking = enable_thinking
        logger.info("APIBackend initialized successfully")

    def generate_batch(self, prompts: List[str], **gen_kwargs) -> List[str]:
        results = []
        logger.info("APIBackend.generate_batch | batch_size=%d", len(prompts))

        for i, prompt in enumerate(prompts):
            try:
                request_kwargs = {
                    "model": self.model,
                    "messages": [
                        {"role": "system", "content": ""},
                        {"role": "user", "content": prompt},
                    ],
                    "max_tokens": gen_kwargs.get("max_new_tokens", 128),
                }

                # ---------- 随机性参数（二选一） ----------
                temperature = gen_kwargs.get("temperature", None)
                top_p = gen_kwargs.get("top_p", None)

                if temperature is not None:
                    request_kwargs["temperature"] = temperature
                elif top_p is not None:
                    request_kwargs["top_p"] = top_p

                # ---------- thinking / reasoning ----------
                # 非 streaming 场景，必须关
                request_kwargs["stream"] = False
                request_kwargs["extra_body"] = {
                    "enable_thinking": self.enable_thinking
                }

                resp = self.client.chat.completions.create(**request_kwargs)

                results.append(resp.choices[0].message.content.strip())

            except Exception:
                logger.exception(
                    "APIBackend error on prompt %d/%d", i + 1, len(prompts)
                )
                results.append("")

        return results


# backend.py

import logging
from abc import ABC, abstractmethod
from typing import List, Optional

logger = logging.getLogger(__name__)

# ===============================
# Backend abstract base class
# ===============================

class Backend(ABC):
    """
    Abstract backend interface.
    """

    @abstractmethod
    def generate_batch(self, prompts: List[str], **gen_kwargs) -> List[str]:
        raise NotImplementedError


# ===============================
# Local vLLM backend
# ===============================

class LocalBackend(Backend):
    """
    Local vLLM backend (token-level, batch inference).
    """

    def __init__(
        self,
        model_path: str,
        dtype: str = "auto",
        trust_remote_code: bool = False,
        tensor_parallel_size: int = 1,
        gpu_memory_utilization: float = 0.98,
        max_length: int = 2048,
        stop_words: Optional[list[str]] = None,
    ):
        from transformers import AutoTokenizer
        from vllm import LLM

        logger.info(
            "Initializing LocalBackend | model=%s | dtype=%s | tp=%d | max_length=%d",
            model_path,
            dtype,
            tensor_parallel_size,
            max_length,
        )

        self.model = LLM(
            model=model_path,
            dtype=dtype,
            trust_remote_code=trust_remote_code,
            tensor_parallel_size=tensor_parallel_size,
            gpu_memory_utilization=gpu_memory_utilization,
        )

        self.tokenizer = AutoTokenizer.from_pretrained(
            model_path,
            trust_remote_code=trust_remote_code,
            truncation_side="left",
            padding_side="right",
        )

        if not self.tokenizer.eos_token:
            logger.warning("Tokenizer has no eos_token, using bos_token instead")
            self.tokenizer.eos_token = self.tokenizer.bos_token
        self.tokenizer.pad_token = self.tokenizer.eos_token

        self.max_length = max_length
        self.stop_words = stop_words or ["[/ANSWER]"]

        logger.info("LocalBackend initialized successfully")

    def generate_batch(self, prompts: List[str], **gen_kwargs) -> List[str]:
        from vllm import SamplingParams
        import time

        batch_size = len(prompts)
        logger.debug("LocalBackend.generate_batch | batch_size=%d", batch_size)

        enc = self.tokenizer(
            prompts,
            truncation=True,
            max_length=self.max_length,
            padding=False,
        )

        input_ids = enc["input_ids"]   # List[List[int]]
        input_lens = [len(ids) for ids in input_ids]

        max_new_tokens = int(gen_kwargs.get("max_new_tokens", 128))
        max_tokens = min(
            max_new_tokens,
            min(self.max_length - l for l in input_lens),
        )

        if max_tokens <= 0:
            logger.warning(
                "All prompts too long, skip generation | batch_size=%d", batch_size
            )
            return [""] * batch_size

        sampling_params = SamplingParams(
            temperature=float(gen_kwargs.get("temperature", 0.0)),
            top_p=float(gen_kwargs.get("top_p", 1.0)),
            max_tokens=max_tokens,
            stop=self.stop_words,
        )

        t0 = time.time()
        outputs = self.model.generate(
            prompt_token_ids=input_ids,
            sampling_params=sampling_params,
            use_tqdm=False,
        )
        dt = time.time() - t0

        logger.info(
            "LocalBackend.generate_batch done | batch_size=%d | max_tokens=%d | time=%.2fs",
            batch_size,
            max_tokens,
            dt,
        )

        return [o.outputs[0].text.strip() for o in outputs]


# ===============================
# API backend
# ===============================

class APIBackend(Backend):
    """
    OpenAI / OpenAI-compatible API backend.
    """

    def __init__(
        self,
        base_url: str,
        model: str,
        api_key: Optional[str] = None,
        timeout_s: float = 120.0,
        enable_thinking: bool = False,
    ):
        from openai import OpenAI

        logger.info(
            "Initializing APIBackend | model=%s | base_url=%s",
            model,
            base_url,
        )

        self.client = OpenAI(
            base_url=base_url,
            api_key=api_key,
            timeout=timeout_s,
        )
        self.model = model

        self.enable_thinking = enable_thinking
        logger.info("APIBackend initialized successfully")

    def generate_batch(self, prompts: List[str], **gen_kwargs) -> List[str]:
        results = []
        logger.info("APIBackend.generate_batch | batch_size=%d", len(prompts))

        for i, prompt in enumerate(prompts):
            try:
                request_kwargs = {
                    "model": self.model,
                    "messages": [
                        {"role": "system", "content": ""},
                        {"role": "user", "content": prompt},
                    ],
                    "max_tokens": gen_kwargs.get("max_new_tokens", 128),
                }

                # ---------- 随机性参数（二选一） ----------
                temperature = gen_kwargs.get("temperature", None)
                top_p = gen_kwargs.get("top_p", None)

                if temperature is not None:
                    request_kwargs["temperature"] = temperature
                elif top_p is not None:
                    request_kwargs["top_p"] = top_p

                # ---------- thinking / reasoning ----------
                # 非 streaming 场景，必须关
                request_kwargs["stream"] = False
                request_kwargs["extra_body"] = {
                    "enable_thinking": self.enable_thinking
                }

                resp = self.client.chat.completions.create(**request_kwargs)

                results.append(resp.choices[0].message.content.strip())

            except Exception:
                logger.exception(
                    "APIBackend error on prompt %d/%d", i + 1, len(prompts)
                )
                results.append("")

        return results


