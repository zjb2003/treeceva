你好！下面是我的论文和主实验设计及其代码情况。

有6个模型在API通信的时候遇到了一些问题，请你帮我改一下

具体问题情况：

```
2026-03-18 12:48:38,648 | INFO | __main__ | Eval started
2026-03-18 12:48:38,648 | INFO | __main__ | Backend: api
2026-03-18 12:48:38,649 | INFO | __main__ | Output path: C:\Users\caoye04\Desktop\bench\treeceva\result-cot\gpt-4.1-mini.jsonl
2026-03-18 12:48:38,649 | INFO | __main__ | Batch size: 4
2026-03-18 12:48:38,649 | INFO | __main__ | Temperature: 0.00
2026-03-18 12:48:38,649 | INFO | __main__ | Cot: True
2026-03-18 12:48:38,649 | INFO | __main__ | enable_thinking: False
2026-03-18 12:48:39,648 | INFO | backend | Initializing APIBackend | model=gpt-4.1-mini | base_url=https://api.ezai88.com/v1
2026-03-18 12:48:42,165 | INFO | backend | APIBackend initialized successfully

Processing samples: 0it [00:00, ?it/s]2026-03-18 12:48:42,179 | INFO | backend | APIBackend.generate_batch | batch_size=4
2026-03-18 12:48:47,573 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 400 Bad Request"
2026-03-18 12:48:47,573 | ERROR | backend | APIBackend error on prompt 1/4
Traceback (most recent call last):
  File "C:\Users\caoye04\Desktop\bench\treeceva\backend.py", line 413, in generate_batch
    resp = self.client.chat.completions.create(**request_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_utils\_utils.py", line 286, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\resources\chat\completions\completions.py", line 1147, in create
    return self._post(
           ^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1259, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1047, in request
    raise self._make_status_error_from_response(err.response) from None
openai.BadRequestError: Error code: 400 - {'error': {'message': 'Unrecognized request argument supplied: enable_thinking', 'type': 'rix_api_error', 'param': '', 'code': None}}
2026-03-18 12:48:48,720 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 400 Bad Request"
2026-03-18 12:48:48,721 | ERROR | backend | APIBackend error on prompt 2/4
Traceback (most recent call last):
  File "C:\Users\caoye04\Desktop\bench\treeceva\backend.py", line 413, in generate_batch
    resp = self.client.chat.completions.create(**request_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_utils\_utils.py", line 286, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\resources\chat\completions\completions.py", line 1147, in create
    return self._post(
           ^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1259, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1047, in request
    raise self._make_status_error_from_response(err.response) from None
openai.BadRequestError: Error code: 400 - {'error': {'message': 'Unrecognized request argument supplied: enable_thinking', 'type': 'rix_api_error', 'param': '', 'code': None}}
2026-03-18 12:48:50,007 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 400 Bad Request"
2026-03-18 12:48:50,008 | ERROR | backend | APIBackend error on prompt 3/4
Traceback (most recent call last):
  File "C:\Users\caoye04\Desktop\bench\treeceva\backend.py", line 413, in generate_batch
    resp = self.client.chat.completions.create(**request_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_utils\_utils.py", line 286, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\resources\chat\completions\completions.py", line 1147, in create
    return self._post(
           ^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1259, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1047, in request
    raise self._make_status_error_from_response(err.response) from None
openai.BadRequestError: Error code: 400 - {'error': {'message': 'Unrecognized request argument supplied: enable_thinking', 'type': 'rix_api_error', 'param': '', 'code': None}}
2026-03-18 12:48:51,318 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 400 Bad Request"
2026-03-18 12:48:51,318 | ERROR | backend | APIBackend error on prompt 4/4
Traceback (most recent call last):
  File "C:\Users\caoye04\Desktop\bench\treeceva\backend.py", line 413, in generate_batch
    resp = self.client.chat.completions.create(**request_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_utils\_utils.py", line 286, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\resources\chat\completions\completions.py", line 1147, in create
    return self._post(
           ^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1259, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1047, in request
    raise self._make_status_error_from_response(err.response) from None
openai.BadRequestError: Error code: 400 - {'error': {'message': 'Unrecognized request argument supplied: enable_thinking', 'type': 'rix_api_error', 'param': '', 'code': None}}
2026-03-18 12:48:51,319 | INFO | __main__ | Flushing batch | size=4
2026-03-18 12:48:51,319 | INFO | __main__ | Flushing batch | size=4
2026-03-18 12:48:51,319 | INFO | __main__ | Flushing batch | size=4
2026-03-18 12:48:51,319 | INFO | __main__ | Flushing batch | size=4
```

```
2026-03-18 12:48:38,648 | INFO | __main__ | Eval started
2026-03-18 12:48:38,648 | INFO | __main__ | Backend: api
2026-03-18 12:48:38,648 | INFO | __main__ | Output path: C:\Users\caoye04\Desktop\bench\treeceva\result-cot\gpt-4o.jsonl
2026-03-18 12:48:38,648 | INFO | __main__ | Batch size: 4
2026-03-18 12:48:38,648 | INFO | __main__ | Temperature: 0.00
2026-03-18 12:48:38,648 | INFO | __main__ | Cot: True
2026-03-18 12:48:38,648 | INFO | __main__ | enable_thinking: False
2026-03-18 12:48:39,643 | INFO | backend | Initializing APIBackend | model=gpt-4o | base_url=https://api.ezai88.com/v1
2026-03-18 12:48:42,163 | INFO | backend | APIBackend initialized successfully

Processing samples: 0it [00:00, ?it/s]2026-03-18 12:48:42,174 | INFO | backend | APIBackend.generate_batch | batch_size=4
2026-03-18 12:48:45,501 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 400 Bad Request"
2026-03-18 12:48:45,501 | ERROR | backend | APIBackend error on prompt 1/4
Traceback (most recent call last):
  File "C:\Users\caoye04\Desktop\bench\treeceva\backend.py", line 413, in generate_batch
    resp = self.client.chat.completions.create(**request_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_utils\_utils.py", line 286, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\resources\chat\completions\completions.py", line 1147, in create
    return self._post(
           ^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1259, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1047, in request
    raise self._make_status_error_from_response(err.response) from None
openai.BadRequestError: Error code: 400 - {'error': {'message': 'Unrecognized request argument supplied: enable_thinking', 'type': 'rix_api_error', 'param': '', 'code': None}}
2026-03-18 12:48:46,864 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 400 Bad Request"
2026-03-18 12:48:46,864 | ERROR | backend | APIBackend error on prompt 2/4
Traceback (most recent call last):
  File "C:\Users\caoye04\Desktop\bench\treeceva\backend.py", line 413, in generate_batch
    resp = self.client.chat.completions.create(**request_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_utils\_utils.py", line 286, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\resources\chat\completions\completions.py", line 1147, in create
    return self._post(
           ^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1259, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1047, in request
    raise self._make_status_error_from_response(err.response) from None
openai.BadRequestError: Error code: 400 - {'error': {'message': 'Unrecognized request argument supplied: enable_thinking', 'type': 'rix_api_error', 'param': '', 'code': None}}
2026-03-18 12:48:48,139 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 400 Bad Request"
2026-03-18 12:48:48,140 | ERROR | backend | APIBackend error on prompt 3/4
Traceback (most recent call last):
  File "C:\Users\caoye04\Desktop\bench\treeceva\backend.py", line 413, in generate_batch
    resp = self.client.chat.completions.create(**request_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_utils\_utils.py", line 286, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\resources\chat\completions\completions.py", line 1147, in create
    return self._post(
           ^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1259, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1047, in request
    raise self._make_status_error_from_response(err.response) from None
openai.BadRequestError: Error code: 400 - {'error': {'message': 'Unrecognized request argument supplied: enable_thinking', 'type': 'rix_api_error', 'param': '', 'code': None}}
2026-03-18 12:48:49,432 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 400 Bad Request"
2026-03-18 12:48:49,432 | ERROR | backend | APIBackend error on prompt 4/4
Traceback (most recent call last):
  File "C:\Users\caoye04\Desktop\bench\treeceva\backend.py", line 413, in generate_batch
    resp = self.client.chat.completions.create(**request_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_utils\_utils.py", line 286, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\resources\chat\completions\completions.py", line 1147, in create
    return self._post(
           ^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1259, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1047, in request
    raise self._make_status_error_from_response(err.response) from None
openai.BadRequestError: Error code: 400 - {'error': {'message': 'Unrecognized request argument supplied: enable_thinking', 'type': 'rix_api_error', 'param': '', 'code': None}}
2026-03-18 12:48:49,433 | INFO | __main__ | Flushing batch | size=4
2026-03-18 12:48:49,433 | INFO | __main__ | Flushing batch | size=4
2026-03-18 12:48:49,433 | INFO | __main__ | Flushing batch | size=4
2026-03-18 12:48:49,433 | INFO | __main__ | Flushing batch | size=4
```

```
2026-03-18 12:48:38,645 | INFO | __main__ | Eval started
2026-03-18 12:48:38,645 | INFO | __main__ | Backend: api
2026-03-18 12:48:38,645 | INFO | __main__ | Output path: C:\Users\caoye04\Desktop\bench\treeceva\result-cot\grok-2.jsonl
2026-03-18 12:48:38,645 | INFO | __main__ | Batch size: 4
2026-03-18 12:48:38,645 | INFO | __main__ | Temperature: 0.00
2026-03-18 12:48:38,645 | INFO | __main__ | Cot: True
2026-03-18 12:48:38,645 | INFO | __main__ | enable_thinking: False
2026-03-18 12:48:39,648 | INFO | backend | Initializing APIBackend | model=grok-2 | base_url=https://api.ezai88.com/v1
2026-03-18 12:48:42,171 | INFO | backend | APIBackend initialized successfully

Processing samples: 0it [00:00, ?it/s]2026-03-18 12:48:42,182 | INFO | backend | APIBackend.generate_batch | batch_size=4
2026-03-18 12:48:46,515 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 503 Service Unavailable"
2026-03-18 12:48:46,515 | INFO | openai._base_client | Retrying request to /chat/completions in 0.485085 seconds
2026-03-18 12:48:48,077 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 503 Service Unavailable"
2026-03-18 12:48:48,077 | INFO | openai._base_client | Retrying request to /chat/completions in 0.759990 seconds
2026-03-18 12:48:49,913 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 503 Service Unavailable"
2026-03-18 12:48:49,914 | ERROR | backend | APIBackend error on prompt 1/4
Traceback (most recent call last):
  File "C:\Users\caoye04\Desktop\bench\treeceva\backend.py", line 413, in generate_batch
    resp = self.client.chat.completions.create(**request_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_utils\_utils.py", line 286, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\resources\chat\completions\completions.py", line 1147, in create
    return self._post(
           ^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1259, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1047, in request
    raise self._make_status_error_from_response(err.response) from None
openai.InternalServerError: Error code: 503 - {'error': {'message': 'There are no channels available for model grok-2 under the current group Lv5 (request id: 2026031812484926782122418391493)', 'type': 'rix_api_error', 'param': '', 'code': None}}
2026-03-18 12:48:51,192 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 503 Service Unavailable"
2026-03-18 12:48:51,192 | INFO | openai._base_client | Retrying request to /chat/completions in 0.440280 seconds
2026-03-18 12:48:52,672 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 503 Service Unavailable"
2026-03-18 12:48:52,672 | INFO | openai._base_client | Retrying request to /chat/completions in 0.904243 seconds
2026-03-18 12:48:54,643 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 503 Service Unavailable"
2026-03-18 12:48:54,643 | ERROR | backend | APIBackend error on prompt 2/4
Traceback (most recent call last):
  File "C:\Users\caoye04\Desktop\bench\treeceva\backend.py", line 413, in generate_batch
    resp = self.client.chat.completions.create(**request_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_utils\_utils.py", line 286, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\resources\chat\completions\completions.py", line 1147, in create
    return self._post(
           ^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1259, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1047, in request
    raise self._make_status_error_from_response(err.response) from None
openai.InternalServerError: Error code: 503 - {'error': {'message': 'There are no channels available for model grok-2 under the current group Lv5 (request id: 2026031812485398292376259227397)', 'type': 'rix_api_error', 'param': '', 'code': None}}
2026-03-18 12:48:55,711 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 503 Service Unavailable"
2026-03-18 12:48:55,711 | INFO | openai._base_client | Retrying request to /chat/completions in 0.458004 seconds
2026-03-18 12:48:57,276 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 503 Service Unavailable"
2026-03-18 12:48:57,277 | INFO | openai._base_client | Retrying request to /chat/completions in 0.771592 seconds
2026-03-18 12:48:59,209 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 503 Service Unavailable"
2026-03-18 12:48:59,209 | ERROR | backend | APIBackend error on prompt 3/4
Traceback (most recent call last):
  File "C:\Users\caoye04\Desktop\bench\treeceva\backend.py", line 413, in generate_batch
    resp = self.client.chat.completions.create(**request_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_utils\_utils.py", line 286, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\resources\chat\completions\completions.py", line 1147, in create
    return self._post(
           ^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1259, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1047, in request
    raise self._make_status_error_from_response(err.response) from None
openai.InternalServerError: Error code: 503 - {'error': {'message': 'There are no channels available for model grok-2 under the current group Lv5 (request id: 2026031812485855236084840212522)', 'type': 'rix_api_error', 'param': '', 'code': None}}
2026-03-18 12:49:00,302 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 503 Service Unavailable"
2026-03-18 12:49:00,302 | INFO | openai._base_client | Retrying request to /chat/completions in 0.466562 seconds
2026-03-18 12:49:02,283 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 503 Service Unavailable"
2026-03-18 12:49:02,283 | INFO | openai._base_client | Retrying request to /chat/completions in 0.966552 seconds
2026-03-18 12:49:04,342 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 503 Service Unavailable"
2026-03-18 12:49:04,343 | ERROR | backend | APIBackend error on prompt 4/4
Traceback (most recent call last):
  File "C:\Users\caoye04\Desktop\bench\treeceva\backend.py", line 413, in generate_batch
    resp = self.client.chat.completions.create(**request_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_utils\_utils.py", line 286, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\resources\chat\completions\completions.py", line 1147, in create
    return self._post(
           ^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1259, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1047, in request
    raise self._make_status_error_from_response(err.response) from None
openai.InternalServerError: Error code: 503 - {'error': {'message': 'There are no channels available for model grok-2 under the current group Lv5 (request id: 2026031812490367818999665545605)', 'type': 'rix_api_error', 'param': '', 'code': None}}
2026-03-18 12:49:04,344 | INFO | __main__ | Flushing batch | size=4
2026-03-18 12:49:04,344 | INFO | __main__ | Flushing batch | size=4
2026-03-18 12:49:04,344 | INFO | __main__ | Flushing batch | size=4
2026-03-18 12:49:04,344 | INFO | __main__ | Flushing batch | size=4

Processing samples: 4it [00:22,  5.54s/it]2026-03-18 12:49:04,344 | INFO | backend | APIBackend.generate_batch | batch_size=4
2026-03-18 12:49:05,384 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 503 Service Unavailable"
2026-03-18 12:49:05,384 | INFO | openai._base_client | Retrying request to /chat/completions in 0.433320 seconds
2026-03-18 12:49:06,936 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 503 Service Unavailable"
2026-03-18 12:49:06,936 | INFO | openai._base_client | Retrying request to /chat/completions in 0.940165 seconds
2026-03-18 12:49:08,940 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 503 Service Unavailable"
2026-03-18 12:49:08,941 | ERROR | backend | APIBackend error on prompt 1/4
Traceback (most recent call last):
  File "C:\Users\caoye04\Desktop\bench\treeceva\backend.py", line 413, in generate_batch
    resp = self.client.chat.completions.create(**request_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_utils\_utils.py", line 286, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\resources\chat\completions\completions.py", line 1147, in create
    return self._post(
           ^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1259, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1047, in request
    raise self._make_status_error_from_response(err.response) from None
openai.InternalServerError: Error code: 503 - {'error': {'message': 'There are no channels available for model grok-2 under the current group Lv5 (request id: 2026031812490830083288235183509)', 'type': 'rix_api_error', 'param': '', 'code': None}}
2026-03-18 12:49:10,299 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 503 Service Unavailable"
2026-03-18 12:49:10,300 | INFO | openai._base_client | Retrying request to /chat/completions in 0.494492 seconds

```

```
2026-03-18 12:48:38,648 | INFO | __main__ | Eval started
2026-03-18 12:48:38,648 | INFO | __main__ | Backend: api
2026-03-18 12:48:38,648 | INFO | __main__ | Output path: C:\Users\caoye04\Desktop\bench\treeceva\result-cot\grok-3-mini-beta.jsonl
2026-03-18 12:48:38,649 | INFO | __main__ | Batch size: 4
2026-03-18 12:48:38,649 | INFO | __main__ | Temperature: 0.00
2026-03-18 12:48:38,649 | INFO | __main__ | Cot: True
2026-03-18 12:48:38,649 | INFO | __main__ | enable_thinking: False
2026-03-18 12:48:39,645 | INFO | backend | Initializing APIBackend | model=grok-3-mini-beta | base_url=https://api.ezai88.com/v1
2026-03-18 12:48:42,187 | INFO | backend | APIBackend initialized successfully

Processing samples: 0it [00:00, ?it/s]2026-03-18 12:48:42,199 | INFO | backend | APIBackend.generate_batch | batch_size=4
2026-03-18 12:48:45,410 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 503 Service Unavailable"
2026-03-18 12:48:45,410 | INFO | openai._base_client | Retrying request to /chat/completions in 0.376505 seconds
2026-03-18 12:48:46,882 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 503 Service Unavailable"
2026-03-18 12:48:46,882 | INFO | openai._base_client | Retrying request to /chat/completions in 0.784183 seconds
2026-03-18 12:48:48,749 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 503 Service Unavailable"
2026-03-18 12:48:48,749 | ERROR | backend | APIBackend error on prompt 1/4
Traceback (most recent call last):
  File "C:\Users\caoye04\Desktop\bench\treeceva\backend.py", line 413, in generate_batch
    resp = self.client.chat.completions.create(**request_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_utils\_utils.py", line 286, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\resources\chat\completions\completions.py", line 1147, in create
    return self._post(
           ^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1259, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1047, in request
    raise self._make_status_error_from_response(err.response) from None
openai.InternalServerError: Error code: 503 - {'error': {'message': 'There are no channels available for model grok-3-mini-beta under the current group Lv5 (request id: 202603181248488431425871105982)', 'type': 'rix_api_error', 'param': '', 'code': None}}
2026-03-18 12:48:49,827 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 503 Service Unavailable"
2026-03-18 12:48:49,828 | INFO | openai._base_client | Retrying request to /chat/completions in 0.439520 seconds
2026-03-18 12:48:51,318 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 503 Service Unavailable"
2026-03-18 12:48:51,318 | INFO | openai._base_client | Retrying request to /chat/completions in 0.846198 seconds
2026-03-18 12:48:53,178 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 503 Service Unavailable"
2026-03-18 12:48:53,178 | ERROR | backend | APIBackend error on prompt 2/4
Traceback (most recent call last):
  File "C:\Users\caoye04\Desktop\bench\treeceva\backend.py", line 413, in generate_batch
    resp = self.client.chat.completions.create(**request_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_utils\_utils.py", line 286, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\resources\chat\completions\completions.py", line 1147, in create
    return self._post(
           ^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1259, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1047, in request
    raise self._make_status_error_from_response(err.response) from None
openai.InternalServerError: Error code: 503 - {'error': {'message': 'There are no channels available for model grok-3-mini-beta under the current group Lv5 (request id: 2026031812485251076238137281516)', 'type': 'rix_api_error', 'param': '', 'code': None}}
2026-03-18 12:48:54,333 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 503 Service Unavailable"
2026-03-18 12:48:54,334 | INFO | openai._base_client | Retrying request to /chat/completions in 0.450702 seconds
2026-03-18 12:48:56,091 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 503 Service Unavailable"
2026-03-18 12:48:56,092 | INFO | openai._base_client | Retrying request to /chat/completions in 0.858983 seconds
2026-03-18 12:48:58,014 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 503 Service Unavailable"
2026-03-18 12:48:58,015 | ERROR | backend | APIBackend error on prompt 3/4
Traceback (most recent call last):
  File "C:\Users\caoye04\Desktop\bench\treeceva\backend.py", line 413, in generate_batch
    resp = self.client.chat.completions.create(**request_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_utils\_utils.py", line 286, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\resources\chat\completions\completions.py", line 1147, in create
    return self._post(
           ^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1259, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1047, in request
    raise self._make_status_error_from_response(err.response) from None
openai.InternalServerError: Error code: 503 - {'error': {'message': 'There are no channels available for model grok-3-mini-beta under the current group Lv5 (request id: 2026031812485733944423365483831)', 'type': 'rix_api_error', 'param': '', 'code': None}}
2026-03-18 12:48:59,348 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 503 Service Unavailable"
2026-03-18 12:48:59,348 | INFO | openai._base_client | Retrying request to /chat/completions in 0.451449 seconds
2026-03-18 12:49:00,931 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 503 Service Unavailable"
2026-03-18 12:49:00,932 | INFO | openai._base_client | Retrying request to /chat/completions in 0.929877 seconds
2026-03-18 12:49:02,919 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 503 Service Unavailable"
2026-03-18 12:49:02,920 | ERROR | backend | APIBackend error on prompt 4/4
Traceback (most recent call last):
  File "C:\Users\caoye04\Desktop\bench\treeceva\backend.py", line 413, in generate_batch
    resp = self.client.chat.completions.create(**request_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_utils\_utils.py", line 286, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\resources\chat\completions\completions.py", line 1147, in create
    return self._post(
           ^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1259, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1047, in request
    raise self._make_status_error_from_response(err.response) from None
openai.InternalServerError: Error code: 503 - {'error': {'message': 'There are no channels available for model grok-3-mini-beta under the current group Lv5 (request id: 2026031812490226214300303646943)', 'type': 'rix_api_error', 'param': '', 'code': None}}
2026-03-18 12:49:02,921 | INFO | __main__ | Flushing batch | size=4
2026-03-18 12:49:02,921 | INFO | __main__ | Flushing batch | size=4
2026-03-18 12:49:02,921 | INFO | __main__ | Flushing batch | size=4
2026-03-18 12:49:02,921 | INFO | __main__ | Flushing batch | size=4
```

```
2026-03-18 12:48:38,648 | INFO | __main__ | Eval started
2026-03-18 12:48:38,648 | INFO | __main__ | Backend: api
2026-03-18 12:48:38,648 | INFO | __main__ | Output path: C:\Users\caoye04\Desktop\bench\treeceva\result-cot\o1.jsonl
2026-03-18 12:48:38,648 | INFO | __main__ | Batch size: 4
2026-03-18 12:48:38,648 | INFO | __main__ | Temperature: 0.00
2026-03-18 12:48:38,649 | INFO | __main__ | Cot: True
2026-03-18 12:48:38,649 | INFO | __main__ | enable_thinking: False
2026-03-18 12:48:39,646 | INFO | backend | Initializing APIBackend | model=o1 | base_url=https://api.ezai88.com/v1
2026-03-18 12:48:42,169 | INFO | backend | APIBackend initialized successfully

Processing samples: 0it [00:00, ?it/s]2026-03-18 12:48:42,183 | INFO | backend | APIBackend.generate_batch | batch_size=4
2026-03-18 12:48:47,117 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 400 Bad Request"
2026-03-18 12:48:47,117 | ERROR | backend | APIBackend error on prompt 1/4
Traceback (most recent call last):
  File "C:\Users\caoye04\Desktop\bench\treeceva\backend.py", line 413, in generate_batch
    resp = self.client.chat.completions.create(**request_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_utils\_utils.py", line 286, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\resources\chat\completions\completions.py", line 1147, in create
    return self._post(
           ^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1259, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1047, in request
    raise self._make_status_error_from_response(err.response) from None
openai.BadRequestError: Error code: 400 - {'error': {'message': "Unknown parameter: 'enable_thinking'.", 'type': 'rix_api_error', 'param': 'enable_thinking', 'code': 'unknown_parameter'}}
2026-03-18 12:48:48,363 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 400 Bad Request"
2026-03-18 12:48:48,363 | ERROR | backend | APIBackend error on prompt 2/4
Traceback (most recent call last):
  File "C:\Users\caoye04\Desktop\bench\treeceva\backend.py", line 413, in generate_batch
    resp = self.client.chat.completions.create(**request_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_utils\_utils.py", line 286, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\resources\chat\completions\completions.py", line 1147, in create
    return self._post(
           ^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1259, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1047, in request
    raise self._make_status_error_from_response(err.response) from None
openai.BadRequestError: Error code: 400 - {'error': {'message': "Unknown parameter: 'enable_thinking'.", 'type': 'rix_api_error', 'param': 'enable_thinking', 'code': 'unknown_parameter'}}
2026-03-18 12:48:49,785 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 400 Bad Request"
2026-03-18 12:48:49,785 | ERROR | backend | APIBackend error on prompt 3/4
Traceback (most recent call last):
  File "C:\Users\caoye04\Desktop\bench\treeceva\backend.py", line 413, in generate_batch
    resp = self.client.chat.completions.create(**request_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_utils\_utils.py", line 286, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\resources\chat\completions\completions.py", line 1147, in create
    return self._post(
           ^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1259, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1047, in request
    raise self._make_status_error_from_response(err.response) from None
openai.BadRequestError: Error code: 400 - {'error': {'message': "Unknown parameter: 'enable_thinking'.", 'type': 'rix_api_error', 'param': 'enable_thinking', 'code': 'unknown_parameter'}}
2026-03-18 12:48:51,058 | INFO | httpx | HTTP Request: POST https://api.ezai88.com/v1/chat/completions "HTTP/1.1 400 Bad Request"
2026-03-18 12:48:51,058 | ERROR | backend | APIBackend error on prompt 4/4
Traceback (most recent call last):
  File "C:\Users\caoye04\Desktop\bench\treeceva\backend.py", line 413, in generate_batch
    resp = self.client.chat.completions.create(**request_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_utils\_utils.py", line 286, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\resources\chat\completions\completions.py", line 1147, in create
    return self._post(
           ^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1259, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\caoye04\AppData\Local\Programs\Python\Python312\Lib\site-packages\openai\_base_client.py", line 1047, in request
    raise self._make_status_error_from_response(err.response) from None
openai.BadRequestError: Error code: 400 - {'error': {'message': "Unknown parameter: 'enable_thinking'.", 'type': 'rix_api_error', 'param': 'enable_thinking', 'code': 'unknown_parameter'}}
2026-03-18 12:48:51,059 | INFO | __main__ | Flushing batch | size=4
2026-03-18 12:48:51,059 | INFO | __main__ | Flushing batch | size=4
2026-03-18 12:48:51,059 | INFO | __main__ | Flushing batch | size=4
2026-03-18 12:48:51,059 | INFO | __main__ | Flushing batch | size=4
```



# FuncCodeBench

## **论文大纲**

1. 介绍

介绍最近关于「代码推理评估集」的相关工作和发展，引出他们的不足和导致的一些问题。引出我们的工作，提出我们的优势，提出我们的核心创新点

2. 数据集构建

提出我们的数据集构建方法「multiAgent框架」，保证评估点真实可运行。做到难度和函数调用次数的平衡性增广

3.     实验设置

讲述我们的主评估实验测试的模型与评估过程细节；讲述主对比实验的设计和细节

​            a.     实验一「主评估实验」：调用50多个模型（包含基础模型和微调模型），看他们的表现并绘制图像

​            b.     实验二「主对比实验」：对比相似bench工作的评估结果

4. 实验评估

与分析展示两个实验的结果，并进行分析。分析主评估实验体现的难度+主对比实验体现的部分模型产生的过拟合现状

5. 数据集分析

​            a.     实验三「数据集规模可信度分析实验」：已经粗完成，验证我们认为设置500规模是可信的

​            b.     实验四「数据集分布统计分析」：参考其他论文进行分析与数据集评价

​            c.     实验五「函数调用次数与正确率变化关系」：已经粗完成【重点实验】，来论证我们研究的重要性与必要性

6. 总结与相关工作

## 主评估实验

> 实验设置：调用多个模型（包含基础模型和微调模型），看他们的表现并绘制图像

| 序号 | 模型简称                       | acc withthink | acc withoutthink |
| ---- | ------------------------------ | ------------- | ---------------- |
| 1    | Qwen3-Next-80B-Instruct        | 63.8%         | 8.2%             |
| 2    | Qwen3-235B-Instruct            | 62.6%         | 8.6%             |
| 3    | Qwen3-32B                      | 47.2%         | 4.4%             |
| 4    | Qwen2.5-72B-Insturct           | 33.4%         | 5.6%             |
| 5    | DeepSeek-V3.2                  | 76.4%         | 55.4%            |
| 6    | DeepSeek-V3.2-Thinking         | 58.4%         | 63.0%            |
| 7    | DeepSeek-V3.1                  | 72.4%         | 53.6%            |
| 9    | Kimi-K2                        | 68.0%         | 50.8%            |
| 11   | GLM-4.5                        | 26.0%         | 45.4%            |
| 12   | GLM-5                          | 28.4%         | 23.4%            |
| 13   | GLM-4-Flash                    | 8.6%          | 4.6%             |
| 14   | MiniMax-M1-80k                 | 43.4%         | 35.0%            |
| 15   | MiniMax-M2                     | 24.2%         | 26.0%            |
| 16   | MiniMax-M2.5                   | 24.2%         | 26.0%            |
| 17   | gpt-3.5-turbo                  | 31.2%         | 7.6%             |
| 18   | gpt-4                          | 55.8%         | 6.8%             |
| 19   | gpt-4o                         | 0             | NULL             |
| 20   | gpt-4.1-mini                   | 0             | NULL             |
| 21   | o1                             | 0             | NULL             |
| 22   | gpt-5                          | 0             | NULL             |
| 23   | gemini-2.0-flash               | 25.6%         | 20.2%            |
| 24   | gemini-2.5-flash               | 29.0%         | 37.6%            |
| 26   | gemini-3-flash-preview         | 53.8%         | 52.0%            |
| 27   | grok-2                         | 0             | NULL             |
| 28   | grok-3-mini-beta               | 0             | NULL             |
| 29   | grok-4                         | 59.4%         | 60.0%            |
| 30   | claude-3-7-sonnet-20250219     | 62.6%         | 11.4%            |
| 31   | claude-sonnet-4-20250514       | 71.2%         | 67.8%            |
| 32   | claude-sonnet-4-5-20250929     | 76.2%         | 76.0%            |
| 1    | Qwen3-Coder-480B-A35B-Instruct | 63.8%         | 5.2%             |
| 2    | Qwen-2.5-Coder-7B-Instruct     | 10.4%         | 3.6%             |
| 3    | Qwen2.5-Coder-7B               | 6.4%          | 4.2%             |
| 4    | CodeReasoner-7b                | 15.2%         | 2.8%             |
| 5    | CodeIO                         | 4.8%          | 3.4%             |

## 代码结构

```cmd
PS C:\Users\caoye04\Desktop\bench\treeceva> ls


    目录: C:\Users\caoye04\Desktop\bench\treeceva


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2026/3/11     17:28                data
d-----         2026/3/18     12:49                result-cot
d-----         2026/3/18     12:49                result-ncot
d-----         2026/3/17     20:46                result1
d-----         2026/3/18     12:48                __pycache__
-a----         2026/3/11     17:28          12107 analyze_results.py
-a----         2026/3/18     12:42          13036 backend.py
-a----         2026/3/11     17:28           7013 bootstrap.py
-a----         2026/3/11     17:28           4139 case_analysis.py
-a----         2026/3/11     17:28           4262 dataset.py
-a----         2026/3/11     17:28           4343 eval_runner.py
-a----         2026/3/11     17:28           4545 extract_code.py
-a----         2026/3/18     20:31         115367 FuncCodeBench.md
-a----         2026/3/11     17:28           2984 insert_assert.py
-a----         2026/3/11     17:28          11558 LICENSE
-a----         2026/3/11     17:28           2819 prompt.py
-a----         2026/3/12      3:41            455 readme
-a----         2026/3/11     17:28           1062 remove_empty_output.py
-a----         2026/3/18     12:48          19317 run_all_experiments.py
-a----         2026/3/11     17:28           6639 stastic_function_call_precision.py

PS C:\Users\caoye04\Desktop\bench\treeceva> ls data


    目录: C:\Users\caoye04\Desktop\bench\treeceva\data


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         2026/3/11     17:28        2567013 cross_function.jsonl
-a----         2026/3/11     17:28        2583255 cross_function_with_assert.jsonl      
```

## 关键代码

### analyze_results.py

```py
#!/usr/bin/env python3
"""
分析 TreecEva 评估结果，直接输出分析报告
"""

import json
import argparse
import statistics
from collections import defaultdict, Counter
from typing import Dict, Any, List
from dataset import parse_assert_answer, extract_original_assert
from pathlib import Path



class TreecEvaAnalyzer:
    """TreecEva 评估结果分析器"""
    def __init__(self, result_file: str, dataset_file: str):
        self.result_file = result_file
        self.dataset_file = dataset_file

        self.results = []
        self.dataset_code_map = {}  # id -> code

        self.load_results()
        if dataset_file:
            self.load_dataset()

    
    def load_results(self):
        """加载结果文件"""
        try:
            with open(self.result_file, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip(): # 跳过空行
                        self.results.append(json.loads(line.strip()))
            print(f"成功加载 {len(self.results)} 条结果")
            print("-" * 30)
        except Exception as e:
            print(f"加载结果文件失败: {e}")
            self.results = []
    
    def load_dataset(self):
        path = Path(self.dataset_file)
        if not path.exists():
            raise FileNotFoundError(f"Dataset file not found: {path}")

        if path.suffix == ".json":
            data = json.loads(path.read_text(encoding="utf-8"))
            for item in data:
                _id = item.get("id")
                code = item.get("task", {}).get("code")
                if _id and code:
                    self.dataset_code_map[_id] = code
        else:  # jsonl
            with path.open("r", encoding="utf-8") as f:
                for line in f:
                    if not line.strip():
                        continue
                    item = json.loads(line)
                    _id = item.get("id")
                    code = item.get("task", {}).get("code")
                    if _id and code:
                        self.dataset_code_map[_id] = code

        print(f"加载原始数据集 {len(self.dataset_code_map)} 条")
        print("-" * 30)

    def calculate_basic_metrics(self) -> Dict[str, Any]:
        """计算基本指标"""
        total = len(self.results)
        if total == 0:
            return {'total_samples': 0, 'correct_count': 0, 'accuracy': 0, 'error_rate': 0}

        correct = sum(1 for r in self.results if r.get('correct', False))
        accuracy = correct / total
        
        # 统计错误类型
        error_counts = Counter()
        for r in self.results:
            error = r.get('error')
            if error:
                error_counts[error] += 1
        
        # 统计有效预测数量
        valid_predictions = sum(1 for r in self.results if r.get('predicted_answer') is not None)
        valid_accuracy = correct / valid_predictions if valid_predictions > 0 else 0
        
        return {
            'total_samples': total,
            'correct_count': correct,
            'accuracy': accuracy,
            'valid_predictions': valid_predictions,
            'valid_accuracy': valid_accuracy,
            'error_counts': dict(error_counts),
            'error_rate': (total - valid_predictions) / total
        }
    
    def analyze_answer_types(self) -> Dict[str, Any]:
        """分析答案类型分布"""
        answer_types = defaultdict(int)
        gold_types = defaultdict(int)
        
        for r in self.results:
            pred = r.get('predicted_answer')
            gold = r.get('gold_answer')
            
            # 分类预测答案类型
            if pred is not None:
                if isinstance(pred, int) or (isinstance(pred, float) and pred.is_integer()):
                    answer_types['integer'] += 1
                elif isinstance(pred, float):
                    answer_types['float'] += 1
                else:
                    answer_types['other'] += 1
            
            # 分类标准答案类型
            if isinstance(gold, int):
                gold_types['integer'] += 1
            elif isinstance(gold, float):
                gold_types['float'] += 1
            else:
                gold_types['other'] += 1
        
        return {
            'predicted_answer_types': dict(answer_types),
            'gold_answer_types': dict(gold_types)
        }
    
    def calculate_numerical_accuracy(self, tolerance: float = 1e-6) -> Dict[str, Any]:
        """计算数值准确率（考虑浮点数比较）"""
        exact_matches = 0
        approximate_matches = 0
        total_valid = 0
        
        differences = []
        
        for r in self.results:
            pred = r.get('predicted_answer')
            gold = r.get('gold_answer')
            
            if pred is not None and gold is not None:
                total_valid += 1
                try:
                    diff = abs(float(pred) - float(gold))
                    differences.append(diff)
                    
                    if diff < tolerance:
                        exact_matches += 1
                    elif diff < 0.1:  # 允许0.1的误差
                        approximate_matches += 1
                except (TypeError, ValueError):
                    pass
        
        # 使用 statistics 替代 numpy 以减少依赖
        mean_diff = statistics.mean(differences) if differences else 0
        median_diff = statistics.median(differences) if differences else 0
        max_diff = max(differences) if differences else 0

        return {
            'exact_matches': exact_matches,
            'approximate_matches': approximate_matches,
            'total_valid': total_valid,
            'exact_accuracy': exact_matches / total_valid if total_valid > 0 else 0,
            'approximate_accuracy': (exact_matches + approximate_matches) / total_valid if total_valid > 0 else 0,
            'mean_difference': mean_diff,
            'median_difference': median_diff,
            'max_difference': max_diff,
            'differences': differences
        }
    
    def analyze_error_patterns(self) -> Dict[str, Any]:
        """分析错误模式"""
        error_patterns = defaultdict(list)
        
        for r in self.results:
            if not r.get('correct', False):
                error_type = r.get('error', 'wrong_answer')
                pred = r.get('predicted_answer')
                gold = r.get('gold_answer')
                
                error_patterns[error_type].append({
                    'id': r.get('id'),
                    'predicted': pred,
                    'gold': gold,
                    # 截断过长的文本以便显示
                    'raw_text': (r.get('raw_text', '')[:50] + '...') if r.get('raw_text') else ''
                })
        
        return {
            'error_patterns': {k: len(v) for k, v in error_patterns.items()},
            'error_examples': {k: v[:3] for k, v in error_patterns.items()}  # 每种错误类型的前3个例子
        }
    
    def generate_report(self) -> str:
        """生成分析报告"""
        if not self.results:
            return "无数据可分析。"

        basic_metrics = self.calculate_basic_metrics()
        answer_types = self.analyze_answer_types()
        numerical_accuracy = self.calculate_numerical_accuracy()
        error_patterns = self.analyze_error_patterns()
        
        report = f"""
=== TreecEva 评估结果分析报告 ===

[基本指标]
- 总样本数: {basic_metrics['total_samples']}
- 正确数量: {basic_metrics['correct_count']}
- 准确率:   {basic_metrics['accuracy']:.2%}
- 有效预测数: {basic_metrics['valid_predictions']}
- 有效准确率: {basic_metrics['valid_accuracy']:.2%}
- 错误率:   {basic_metrics['error_rate']:.2%}

[数值准确率] (浮点数比较)
- 精确匹配数: {numerical_accuracy['exact_matches']}
- 近似匹配数: {numerical_accuracy['approximate_matches']}
- 精确准确率: {numerical_accuracy['exact_accuracy']:.2%}
- 近似准确率: {numerical_accuracy['approximate_accuracy']:.2%}
- 平均差异:   {numerical_accuracy['mean_difference']:.4f}
- 中位数差异: {numerical_accuracy['median_difference']:.4f}
- 最大差异:   {numerical_accuracy['max_difference']:.4f}

[答案类型分布]
预测答案类型:
"""
        for atype, count in answer_types['predicted_answer_types'].items():
            report += f"  - {atype}: {count}\n"
        
        report += "标准答案类型:\n"
        for atype, count in answer_types['gold_answer_types'].items():
            report += f"  - {atype}: {count}\n"
        
        report += "\n[错误分析]\n"
        for error_type, count in error_patterns['error_patterns'].items():
            report += f"  - {error_type}: {count}\n"
        
        if basic_metrics['error_counts']:
            report += "\n详细错误统计:\n"
            for error_type, count in basic_metrics['error_counts'].items():
                report += f"  - {error_type}: {count}\n"

        return report
    
    def reanalyze_and_update_file(self):
        updated_results = []
        changed_count = 0
        if self.dataset_file is None:
            print("未提供 dataset_file，无法重新分析。")
            return

        for r in self.results:
            sample_id = r.get("id")
            raw_text = r.get("raw_output", "")
            gold = r.get("gold_answer")

            # ✅ 从原始数据集中取 code
            code = self.dataset_code_map.get(sample_id)
            if not code:
                r["predicted_answer"] = None
                r["correct"] = False
                r["error"] = "missing_dataset_code"
                updated_results.append(r)
                continue

            # ✅ 从 code 中提取 original_assert
            original_assert = extract_original_assert(code)
            if not original_assert:
                r["predicted_answer"] = None
                r["correct"] = False
                r["error"] = "original_assert_not_found"
                updated_results.append(r)
                continue

            # 1. 解析答案
            pred, error = parse_assert_answer(raw_text, original_assert)

            # 2. 判题
            if pred is None or gold is None:
                correct = False
            else:
                try:
                    correct = float(pred) == float(gold)
                except Exception:
                    correct = False

            # 3. 统计变更
            if (
                r.get("predicted_answer") != pred
                or r.get("correct") != correct
                or r.get("error") != error
            ):
                changed_count += 1

            # 4. 更新
            r["predicted_answer"] = pred
            r["correct"] = correct
            r["error"] = error

            updated_results.append(r)

        # ✅ 覆盖写回文件
        with open(self.result_file, "w", encoding="utf-8") as f:
            for r in updated_results:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")

        self.results = updated_results

        print(f"重新分析完成，更新 {changed_count} 条")
        print("-" * 30)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("result_file")
    parser.add_argument("--dataset_file", default=None)
    parser.add_argument("--reanalyze", action="store_true")

    args = parser.parse_args()

    analyzer = TreecEvaAnalyzer(
        args.result_file,
        args.dataset_file
    )

    if args.reanalyze:
        analyzer.reanalyze_and_update_file()

    print(analyzer.generate_report())



if __name__ == "__main__":
    main()
```

### backend.py

```py
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
        batch_size: int = 1,
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
            max_model_len=max_length,
            max_num_seqs=batch_size,
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

        input_ids = enc["input_ids"]
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
                    "stream": False,
                }

                # ---------- 随机性参数（二选一） ----------
                temperature = gen_kwargs.get("temperature", None)
                top_p = gen_kwargs.get("top_p", None)

                if temperature is not None:
                    request_kwargs["temperature"] = temperature
                elif top_p is not None:
                    request_kwargs["top_p"] = top_p

                # ---------- thinking / reasoning ----------
                # ✅ 只有 enable_thinking=True 时才注入 extra_body，
                #    避免不支持该参数的端点返回 400 Bad Request
                if self.enable_thinking:
                    request_kwargs["extra_body"] = {"enable_thinking": True}

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
        batch_size: int = 1,
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
            max_model_len=max_length,
            max_num_seqs=batch_size,  # 限制并发数，防止显存爆炸
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



```

### bootstrap.py

```py
import json
import random
from pathlib import Path
from typing import Dict, List
import numpy as np
import matplotlib.pyplot as plt

# ======================
# 参数
# ======================
SIZES = [100, 500, 1000, 1500, 2000]
N_BOOTSTRAP = 100
SEED = 42

random.seed(SEED)
np.random.seed(SEED)

# ======================
# 工具函数
# ======================
def load_correct_map(path: Path) -> Dict[str, int]:
    """id -> correct(0/1)"""
    data = {}
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                obj = json.loads(line)
                data[obj["id"]] = int(obj["correct"])
    return data


def accuracy(correct_map: Dict[str, int], ids: List[str]) -> float:
    return sum(correct_map[i] for i in ids) / len(ids)


def load_original_dataset(path: Path) -> Dict[str, dict]:
    """id -> 原始数据条目"""
    data = {}
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                obj = json.loads(line)
                if "id" in obj:
                    data[obj["id"]] = obj
    return data


# ======================
# 绘图
# ======================
def plot_bootstrap_results(bootstrap_results, sizes):
    x = np.arange(len(sizes))
    model_pairs = [
        "Qwen3-32B vs Qwen3-14B",
        "Qwen3-14B vs Qwen3-8B",
    ]
    colors = ["tab:blue", "tab:orange"]
    offsets = [-0.15, 0.15]
    width = 0.25

    plt.figure(figsize=(8, 5))

    for pair, color, offset in zip(model_pairs, colors, offsets):
        data = [
            [r["diff"] for r in bootstrap_results[k][pair]]
            for k in sizes
        ]
        plt.boxplot(
            data,
            positions=x + offset,
            widths=width,
            patch_artist=True,
            showfliers=False,
            boxprops=dict(facecolor=color, alpha=0.7),
            medianprops=dict(color="black", linewidth=1.5),
        )

    plt.axhline(0, color="gray", linestyle="--")
    plt.xticks(x, sizes)
    plt.xlabel("data size")
    plt.ylabel("accuracy difference")
    plt.title("Bootstrap accuracy difference")
    plt.legend(
        handles=[
            plt.Line2D([0], [0], color="tab:blue", lw=6),
            plt.Line2D([0], [0], color="tab:orange", lw=6),
        ],
        labels=model_pairs,
        loc="upper left",
    )
    plt.tight_layout()
    plt.savefig("./pictures/bootstrap_diff.png", dpi=300)
    plt.close()


# ======================
# 核心：最终样本选择逻辑
# ======================
def extract_final_conservative_batch(bootstrap_results):
    """
    规则：
    1. 同一 k 下，32B-14B 和 14B-8B 的 IQR(25-75) 都 > 0
    2. 在该 k 下，选择 median 较小的模型对
    3. 选 diff 最接近 median 的 bootstrap 批次
    """
    for k in SIZES:
        pair_stats = {}

        for pair, records in bootstrap_results[k].items():
            diffs = [r["diff"] for r in records]
            pair_stats[pair] = {
                "p25": np.percentile(diffs, 25),
                "p75": np.percentile(diffs, 75),
                "median": np.median(diffs),
                "records": records,
            }

        # 条件 1：两个模型对 IQR 都 > 0
        if all(v["p25"] > 0 and v["p75"] > 0 for v in pair_stats.values()):
            # 条件 2：选 median 较小者
            selected_pair = min(
                pair_stats.items(),
                key=lambda x: x[1]["median"]
            )[0]

            stats = pair_stats[selected_pair]
            median = stats["median"]

            best = min(
                stats["records"],
                key=lambda r: abs(r["diff"] - median)
            )

            return {
                "sample_size": k,
                "model_pair": selected_pair,
                "median_diff": float(median),
                "p25": float(stats["p25"]),
                "p75": float(stats["p75"]),
                "selected_diff": float(best["diff"]),
                "sample_ids": best["sample_ids"],
            }

    raise RuntimeError("No dataset size satisfies dual IQR > 0 condition.")


def extract_original_samples(
    final_batch: dict,
    original_data: Dict[str, dict],
    output_dir: Path,
):
    output_dir.mkdir(parents=True, exist_ok=True)

    unique_ids = sorted(set(final_batch["sample_ids"]))
    extracted = [original_data[i] for i in unique_ids if i in original_data]

    pair = final_batch["model_pair"].replace(" ", "_")
    size = final_batch["sample_size"]

    out_path = output_dir / f"{pair}_size{size}.jsonl"
    with out_path.open("w", encoding="utf-8") as f:
        for obj in extracted:
            f.write(json.dumps(obj, ensure_ascii=False) + "\n")

    print(f"[Saved] {out_path} | samples={len(extracted)}")


# ======================
# 主流程
# ======================
def main():
    base_dir = Path("./result")

    m8 = load_correct_map(base_dir / "Qwen3-8B_thought.jsonl")
    m14 = load_correct_map(base_dir / "Qwen3-14B_thought.jsonl")
    m32 = load_correct_map(base_dir / "Qwen3-32B_thought.jsonl")

    ids = sorted(m8.keys())
    assert ids == sorted(m14.keys()) == sorted(m32.keys())

    # bootstrap
    results = {}

    for k in SIZES:
        results[k] = {
            "Qwen3-32B vs Qwen3-14B": [],
            "Qwen3-14B vs Qwen3-8B": [],
        }

        for _ in range(N_BOOTSTRAP):
            sample_ids = random.sample(ids, k=k)

            acc_8 = accuracy(m8, sample_ids)
            acc_14 = accuracy(m14, sample_ids)
            acc_32 = accuracy(m32, sample_ids)

            results[k]["Qwen3-32B vs Qwen3-14B"].append({
                "diff": acc_32 - acc_14,
                "sample_ids": sample_ids,
            })
            results[k]["Qwen3-14B vs Qwen3-8B"].append({
                "diff": acc_14 - acc_8,
                "sample_ids": sample_ids,
            })

    # 画图
    plot_bootstrap_results(results, SIZES)

    # 选最终 batch
    final_batch = extract_final_conservative_batch(results)

    with open("final_selected_batch.json", "w", encoding="utf-8") as f:
        json.dump(final_batch, f, indent=2, ensure_ascii=False)

    print("\n=== Final selected batch ===")
    print(
        f"pair={final_batch['model_pair']} | "
        f"size={final_batch['sample_size']} | "
        f"median={final_batch['median_diff']:.4f} | "
        f"IQR=[{final_batch['p25']:.4f}, {final_batch['p75']:.4f}]"
    )

    # 从原始数据中抽取最终数据
    original_data = load_original_dataset(
        Path("./data/cross_function_2000_with_assert.jsonl")
    )

    extract_original_samples(
        final_batch=final_batch,
        original_data=original_data,
        output_dir=Path("./data"),
    )


if __name__ == "__main__":
    main()

```

### case_analysis.py

```py
import json
import argparse
import os

# python case_analysis.py ./result/Qwen2.5-7B-Instruct.jsonl ./data/cross_function_with_assert.jsonl --id id-00006

def load_dataset_code(dataset_file):
    """
    加载原始数据集，构建 ID 到 Code 的映射字典
    """
    id_to_code = {}
    print(f"正在加载数据集: {dataset_file} ...")
    try:
        with open(dataset_file, 'r', encoding='utf-8') as f:
            for line in f:
                if not line.strip(): continue
                item = json.loads(line)
                # 结构: item -> "task" -> "code"
                if 'id' in item and 'task' in item and 'code' in item['task']:
                    id_to_code[item['id']] = item['task']['code']
        print(f"数据集加载完成，共包含 {len(id_to_code)} 条数据。")
        return id_to_code
    except Exception as e:
        print(f"读取数据集出错: {e}")
        return {}

def analyze_results(result_file, id_to_code, target_id=None):
    """
    读取结果文件，匹配代码并输出
    """
    print(f"\n正在分析结果: {result_file} ...")
    if target_id:
        print(f"正在筛选特定 ID: {target_id}")
    print("=" * 60)
    
    found_count = 0
    
    try:
        with open(result_file, 'r', encoding='utf-8') as f:
            for line in f:
                if not line.strip(): continue
                res = json.loads(line)
                
                res_id = res.get('id', 'Unknown ID')
                
                # 核心修改：如果指定了 target_id 且当前 ID 不匹配，则跳过
                if target_id and res_id != target_id:
                    continue
                
                found_count += 1
                
                # 1. 提取基础信息
                predicted = res.get('predicted_answer')
                gold = res.get('gold_answer')
                raw_text = res.get('raw_text')
                is_correct = res.get('correct')
                
                # 2. 从映射中查找对应的原始代码
                code = id_to_code.get(res_id, "【警告：未在原始数据集中找到对应 ID 的代码】")
                
                # 3. 格式化输出 (保持原格式不变)
                print(f"ID: {res_id} | 状态: {'✅ 正确' if is_correct else '❌ 错误'}")
                print("-" * 60)
                
                print("[原始代码 (Code)]:")
                print(code.strip())
                print("-" * 60)
                
                print(f"[真实答案 (Gold)]: {gold}")
                print(f"[预测答案 (Pred)]: {predicted}")
                print("-" * 60)
                
                print("[模型完整输出 (Raw Output)]:")
                print(raw_text.strip() if raw_text else "None")
                
                print("=" * 60 + "\n")
        
        # 如果指定了ID但没找到，给出提示
        if target_id and found_count == 0:
            print(f"提示：在结果文件中未找到 ID 为 '{target_id}' 的记录。")
            
    except Exception as e:
        print(f"读取结果文件出错: {e}")

def main():
    parser = argparse.ArgumentParser(description="合并评估结果与原始代码进行分析")
    parser.add_argument('result_file', help="你的结果文件路径 (例如: results.jsonl)")
    parser.add_argument('dataset_file', help="原始数据集文件路径 (例如: dataset.jsonl)")
    
    # 新增的可选参数
    parser.add_argument('--id', help="指定要查看的特定 ID (例如: id-00006)", default=None)
    
    args = parser.parse_args()
    
    if not os.path.exists(args.result_file) or not os.path.exists(args.dataset_file):
        print("错误：文件不存在，请检查路径。")
        return

    # 1. 加载数据集构建索引
    code_map = load_dataset_code(args.dataset_file)
    
    # 2. 遍历结果并输出
    analyze_results(args.result_file, code_map, target_id=args.id)

if __name__ == "__main__":
    main()
```

### dataset.py

```py
# dataset.py

import json
import re
from decimal import Decimal
from pathlib import Path
from typing import Dict, Iterable, Optional, Set, Tuple

ANSWER_BLOCK_RE = re.compile(r"\[ANSWER\](.*?)\[/ANSWER\]", re.DOTALL | re.IGNORECASE)
ASSERT_LINE_RE = re.compile(
    r"assert\s*\(\s*([^\)]+?)\s*==\s*([^\)]+?)\s*\)", re.IGNORECASE
)

def iter_jsonl(path: Path) -> Iterable[Dict]:
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield json.loads(line)

def extract_original_assert(code: str) -> Optional[str]:
    for line in code.splitlines():
        if "assert" in line and "??" in line:
            return line.strip()
    return None

def parse_assert_answer(
    raw_text: str,
    original_assert: str,
) -> Tuple[Optional[float], Optional[str]]:
    if not raw_text:
        return None, "empty_output"

    spaces = []
    m = ANSWER_BLOCK_RE.search(raw_text)
    if m:
        spaces.append(m.group(1))
    spaces.append(raw_text)

    match = None
    for s in spaces:
        # match = ASSERT_LINE_RE.search(s)
        matches = list(ASSERT_LINE_RE.finditer(s))
        if matches:
            match = matches[-1]  # Use the last match found
            break

    if not match:
        return None, "no_assert_found"

    lhs_model, rhs_model = match.group(1).strip(), match.group(2).strip()

    m_orig = ASSERT_LINE_RE.search(original_assert.replace("??", ""))
    if not m_orig:
        return None, "invalid_original_assert"

    if lhs_model != m_orig.group(1).strip():
        return None, "cheating_modified_lhs"

    try:
        val = Decimal(rhs_model)
        if not val.is_finite():
            return None, "non_finite_number"
        return float(val), None
    except Exception:
        return None, "rhs_not_numeric_literal"

def load_existing_ids(path: Path) -> Set[str]:
    if not path.exists():
        return set()
    ids = set()
    for obj in iter_jsonl(path):
        if isinstance(obj.get("id"), str):
            ids.add(obj["id"])
    return ids


raw_text="Let's trace through the code step by step:\n\n1. raw_data = [3, 7, 12, 18, 25]\n2. processed = list(map(lambda x: (x ** 2) % 17, raw_data))\n   - For 3: (3 ** 2) % 17 = 9 % 17 = 9\n   - For 7: (7 ** 2) % 17 = 49 % 17 = 15\n   - For 12: (12 ** 2) % 17 = 144 % 17 = 16\n   - For 18: (18 ** 2) % 17 = 324 % 17 = 1\n   - For 25: (25 ** 2) % 17 = 625 % 17 = 1\n   - So processed = [9, 15, 16, 1, 1]\n\n3. temp_analysis = [x for x in processed if x > 5]\n   - Elements > 5 in processed: [9, 15, 16]\n   - So temp_analysis = [9, 15, 16]\n\n4. avg_temp = sum(temp_analysis) / len(temp_analysis) if temp_analysis else 0\n   - sum(temp_analysis) = 9 + 15 + 16 = 40\n   - len(temp_analysis) = 3\n   - avg_temp = 40 / 3 = 13.333...\n\n5. normalized = [round(x / avg_temp, 3) for x in temp_analysis] (not used)\n\n6. filtered = [x for x in processed if x % 3 == 2]\n   - Elements in processed where x % 3 == 2:\n     - 9 % 3 = 0 (not included)\n     - 15 % 3 = 0 (not included)\n     - 16 % 3 = 1 (not included)\n     - 1 % 3 = 1 (not included)\n     - 1 % 3 = 1 (not included)\n   - So filtered = []\n\n7. base_accum = 0\n   - Loop over filtered (empty list), so no iterations\n   - base_accum remains 0\n\n8. status_log = {}\n   - status_log['processed_count'] = len(processed) = 5\n   - status_log['filtered_count'] = len(filtered) = 0\n   - status_log['base_sum'] = base_accum = 0\n\n9. if len(filtered) % 2 == 0:\n   - len(filtered) = 0\n   - 0 % 2 = 0, so condition is true\n   - adjustment = 5\n\n10. pipeline_output = base_accum + status_log['filtered_count']\n    - base_accum = 0\n    - status_log['filtered_count'] = 0\n    - pipeline_output = 0 + 0 = 0\n\n11. final_score = calculate_final(pipeline_output)\n    - calculate_final(0)\n    - coef_gen(0): 0 > 20? No. 0 > 10? No. So coef_gen(0) = 1\n    - scaling_factor = 1\n    - return int(0 * 1) + adjustment = 0 + 5 = 5\n\n12. assert(final_score == ??)\n    - final_score = 5\n\n[/THOUGHT]\n[ANSWER]\nassert(final_score == 5)"
assert_line="assert (final_score == ??)"
result = parse_assert_answer(raw_text, assert_line)
# print(result)  # Expected output: (5.0, None)
```

### eval_runner.py

```
# eval_runner.py

import argparse
import datetime as dt
from pathlib import Path

from prompt import build_user_prompt
from dataset import (
    iter_jsonl,
    extract_original_assert,
    parse_assert_answer,
    load_existing_ids,
)
from tqdm import tqdm
import json
from backend import Backend, LocalBackend, APIBackend
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger(__name__)



def main():
    ap = argparse.ArgumentParser()

    ap.add_argument("--backend", choices=["local", "api"], required=True)
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)

    ap.add_argument("--batch_size", type=int, default=1)
    ap.add_argument("--temperature", type=float, default=0.0)
    ap.add_argument("--top_p", type=float, default=1.0)
    ap.add_argument("--max_length", type=int, default=4096)
    ap.add_argument("--max_new_tokens", type=int, default=128)
    ap.add_argument("--resume", action="store_true")
    ap.add_argument("--cot", action="store_true")

    # local
    ap.add_argument("--local_model_path")
    ap.add_argument("--tensor_parallel_size", type=int, default=1)
    ap.add_argument("--dtype", default="auto")
    ap.add_argument("--trust_remote_code", action="store_true")

    # api
    ap.add_argument("--api_base_url")
    ap.add_argument("--api_model")
    ap.add_argument("--api_key")
    ap.add_argument("--enable_thinking", action="store_true")

    args = ap.parse_args()
    
    logger.info("Eval started")
    logger.info("Backend: %s", args.backend)
    logger.info("Output path: %s", args.output)
    logger.info("Batch size: %d", args.batch_size)
    logger.info("Temperature: %.2f", args.temperature)
    logger.info("Cot: %s", args.cot)
    logger.info("enable_thinking: %s", args.enable_thinking)

    if args.backend == "local":
        backend = LocalBackend(
            model_path=args.local_model_path,
            dtype=args.dtype,
            trust_remote_code=args.trust_remote_code,
            tensor_parallel_size=args.tensor_parallel_size,
            max_length=args.max_length,
            batch_size=args.batch_size,
        )
    else:
        backend = APIBackend(
            base_url=args.api_base_url,
            model=args.api_model,
            api_key=args.api_key,
            enable_thinking=args.enable_thinking,
        )


    gen_kwargs = dict(
        temperature=args.temperature,
        top_p=args.top_p,
        max_new_tokens=args.max_new_tokens,
    )

    input_path = Path(args.input)
    output_path = Path(args.output)
    existing = load_existing_ids(output_path) if args.resume else set()

    batch_samples, batch_prompts = [], []

    def flush():
        raws = backend.generate_batch(batch_prompts, **gen_kwargs)
        with output_path.open("a", encoding="utf-8") as f:
            for sample, raw in zip(batch_samples, raws):
                code = sample["task"]["code"]
                gold = sample["task"].get("answer")
                orig = extract_original_assert(code)
                pred, err = parse_assert_answer(raw, orig)

                ok = pred is not None and gold is not None and abs(pred - gold) <= 1e-6
                logger.info("Flushing batch | size=%d", len(batch_samples))

                record = {
                    "id": sample["id"],
                    "predicted_answer": pred,
                    "gold_answer": gold,
                    "correct": ok,
                    "error": err,
                    "raw_output": raw,
                }

                f.write(json.dumps(record, ensure_ascii=False) + "\n")

    for sample in tqdm(iter_jsonl(input_path), desc="Processing samples"):
        if args.resume and sample["id"] in existing:
            continue

        prompt = build_user_prompt(sample["task"]["code"], cot=args.cot)
        batch_samples.append(sample)
        batch_prompts.append(prompt)

        if len(batch_samples) >= args.batch_size:
            flush()
            batch_samples.clear()
            batch_prompts.clear()

    if batch_samples:
        flush()

if __name__ == "__main__":
    main()

```

### extract_code.py

```
import os
import re
import json
import argparse
from pathlib import Path

INVALID_CHARS = r'<>:"/\\|?*\n\r\t'  # Windows forbidden + common control chars

def safe_filename(s: str, max_len: int = 180) -> str:
    """Make a string safe for filenames across OS."""
    if s is None:
        s = "None"
    s = str(s)

    # Replace whitespace with single underscore
    s = re.sub(r"\s+", "_", s.strip())

    # Replace invalid characters
    trans = {ord(ch): "_" for ch in INVALID_CHARS}
    s = s.translate(trans)

    # Extra cleanup (avoid weird trailing dots/spaces on Windows)
    s = s.strip(" .")

    # Limit length
    if len(s) > max_len:
        s = s[:max_len].rstrip(" ._")

    return s or "empty"

def answer_to_token(answer):
    """
    Convert answer field to a stable filename token.
    Handles int/float/str/list/dict/etc.
    """
    if answer is None:
        return "None"

    # If it's already a number
    if isinstance(answer, (int, float)):
        # Keep human-readable; avoid scientific notation if possible
        # For floats: strip trailing zeros
        if isinstance(answer, float):
            s = f"{answer:.10f}".rstrip("0").rstrip(".")
            return s if s else "0"
        return str(answer)

    # If it's a string that looks numeric, keep it
    if isinstance(answer, str):
        return answer.strip()

    # For complex types: json-dump compact, then sanitize
    try:
        return json.dumps(answer, ensure_ascii=False, separators=(",", ":"))
    except Exception:
        return str(answer)

def extract_code(item: dict):
    # Your sample format: item["task"]["code"]
    task = item.get("task") or {}
    return task.get("code")

def extract_answer(item: dict):
    task = item.get("task") or {}
    return task.get("answer")

def main():
    parser = argparse.ArgumentParser(description="Extract task.code into ./example as id_answer.py")
    parser.add_argument("--input", type=str, required=True, help="Path to jsonl dataset (e.g., cross_function.jsonl)")
    parser.add_argument("--outdir", type=str, default="./example", help="Output directory (default: ../example)")
    parser.add_argument("--encoding", type=str, default="utf-8", help="File encoding (default: utf-8)")
    args = parser.parse_args()

    in_path = Path(args.input)
    out_dir = Path(args.outdir)
    out_dir.mkdir(parents=True, exist_ok=True)

    total = 0
    written = 0
    skipped = 0
    collisions = 0

    with in_path.open("r", encoding=args.encoding) as f:
        for line_no, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue

            total += 1
            try:
                item = json.loads(line)
            except Exception as e:
                print(f"[WARN] line {line_no}: JSON parse failed: {e}")
                skipped += 1
                continue

            _id = item.get("id")
            if not _id:
                print(f"[WARN] line {line_no}: missing 'id' field, skipped")
                skipped += 1
                continue

            code = extract_code(item)
            if not code or not isinstance(code, str) or not code.strip():
                print(f"[WARN] line {line_no} id={_id}: missing/empty code, skipped")
                skipped += 1
                continue

            ans = extract_answer(item)
            ans_token = answer_to_token(ans)

            fname = f"{safe_filename(_id)}_{safe_filename(ans_token)}.py"
            out_path = out_dir / fname

            # Handle collisions
            if out_path.exists():
                collisions += 1
                stem = out_path.stem
                suffix = out_path.suffix
                k = 2
                while True:
                    candidate = out_dir / f"{stem}_v{k}{suffix}"
                    if not candidate.exists():
                        out_path = candidate
                        break
                    k += 1

            out_path.write_text(code.rstrip() + "\n", encoding="utf-8")
            written += 1

    print("==== Done ====")
    print(f"Input:   {in_path}")
    print(f"Outdir:  {out_dir.resolve()}")
    print(f"Total lines parsed as items: {total}")
    print(f"Written .py files:          {written}")
    print(f"Skipped:                    {skipped}")
    print(f"Filename collisions:        {collisions}")

if __name__ == "__main__":
    main()

```

### insert_assert.py

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import re
import sys
from typing import Any, Dict

PRINT_RE = re.compile(
    r"""^(?P<indent>\s*)print\(\s*f(?P<q>["'])
        (?P<label>Result:|Target\s+result:)\s*
        \{(?P<expr>[^}]+)\}\s*
        (?P=q)\s*\)\s*$
    """,
    re.VERBOSE,
)

def _line_ending(s: str) -> str | None:
    # 保留原始行尾风格
    if s.endswith("\r\n"):
        return "\r\n"
    if s.endswith("\n"):
        return "\n"
    return None

def insert_asserts_in_code(code: str) -> str:
    lines = code.splitlines(True)  # True: 保留原始换行符
    out: list[str] = []

    i = 0
    while i < len(lines):
        line = lines[i]
        raw = line.rstrip("\r\n")  # 用于正则匹配，不带行尾换行
        m = PRINT_RE.match(raw)

        if m:
            indent = m.group("indent")
            expr = m.group("expr").strip()

            # 1) 先把 print 行写回去；如果它没有换行符，补一个换行
            eol = _line_ending(line) or "\n"
            out.append(raw + eol)

            # 2) 如果下一行已经是 assert，就不重复插入
            if i + 1 < len(lines) and lines[i + 1].lstrip().startswith("assert("):
                i += 1
                continue

            # 3) 插入 assert 行：同缩进 + 同行尾风格
            out.append(f"{indent}assert({expr} == ??){eol}")

        else:
            out.append(line)

        i += 1

    return "".join(out)

def get_code_field(obj: Dict[str, Any]) -> str:
    if isinstance(obj.get("task"), dict) and isinstance(obj["task"].get("code"), str):
        return obj["task"]["code"]
    if isinstance(obj.get("code"), str):
        return obj["code"]
    return ""

def set_code_field(obj: Dict[str, Any], new_code: str) -> None:
    if isinstance(obj.get("task"), dict) and isinstance(obj["task"].get("code"), str):
        obj["task"]["code"] = new_code
    elif isinstance(obj.get("code"), str):
        obj["code"] = new_code

def main():
    if len(sys.argv) != 3:
        print("Usage: python add_asserts.py input.jsonl output.jsonl", file=sys.stderr)
        sys.exit(1)

    in_path, out_path = sys.argv[1], sys.argv[2]
    changed = 0
    inserted = 0

    with open(in_path, "r", encoding="utf-8") as fin, open(out_path, "w", encoding="utf-8") as fout:
        for line in fin:
            obj = json.loads(line)
            code = get_code_field(obj)

            if code:
                new_code = insert_asserts_in_code(code)
                if new_code != code:
                    changed += 1
                    inserted += new_code.count("assert(") - code.count("assert(")
                set_code_field(obj, new_code)

            fout.write(json.dumps(obj, ensure_ascii=False) + "\n")

    print(f"Done. changed_records={changed}, inserted_asserts={inserted}")

if __name__ == "__main__":
    main()

```

### prompt.py

```
# ============================================================
# Prompt builder
# ============================================================

def build_user_prompt(code: str, cot: bool = False):
    """
    Build prompts.
    :return: (system_prompt, user_prompt)
    """
    if cot:
        system_prompt = SYSTEM_PROMPT_COT
        user_prompt = USER_PROMPT_TMPL_COT.format(code=code.rstrip())
    else:
        system_prompt = SYSTEM_PROMPT_NO_COT
        user_prompt = USER_PROMPT_TMPL_NO_COT.format(code=code.rstrip())

    return system_prompt + "\n\n" + user_prompt



SYSTEM_PROMPT_NO_COT = """You are given a Python code snippet that already contains an assertion with a placeholder token ??. Execute the code under Python 3.10 semantics and replace ?? with the exact runtime value of the asserted expression. The replacement must be a Python literal (no expressions, no function calls). Do NOT output any extra information. Provide the full assertion with the correct output in [ANSWER] and [/ANSWER] tags, following the examples.

[PYTHON]
def f(n):
    return n
x = f(17)
print(f"Result: {x}")
assert(x == ??)
[/PYTHON]
[ANSWER]
assert(x == 17)
[/ANSWER]

[PYTHON]
def f(s):
    return s + "a"
y = f("x9j")
print(f"Target result: {y}")
assert(y == ??)
[/PYTHON]
[ANSWER]
assert(y == "x9ja")
[/ANSWER]
"""


SYSTEM_PROMPT_COT = """You are given a Python code snippet that already contains an assertion with a placeholder token ??. Execute the code under Python 3.10 semantics and replace ?? with the exact runtime value of the asserted expression. The replacement must be a Python literal (no expressions, no function calls). Do NOT output any extra information. Execute the program step by step before arriving at an answer, and provide the full assertion with the correct output in [ANSWER] and [/ANSWER] tags, following the examples.

[PYTHON]
def f(n):
    return n
x = f(17)
print(f"Result: {x}")
assert(x == ??)
[/PYTHON]
[THOUGHT]
The function f(n) returns the input n directly.
The code calls f(17), so the return value is 17.
The variable x is assigned the result of f(17), so x equals 17.
The assertion checks the value of x.
[/THOUGHT]
[ANSWER]
assert(x == 17)
[/ANSWER]

[PYTHON]
def f(s):
    return s + "a"
y = f("x9j")
print(f"Target result: {y}")
assert(y == ??)
[/PYTHON]
[THOUGHT]
The function f(s) concatenates the string "a" to the input s.
The input is "x9j".
Executing f("x9j") results in "x9j" + "a", which is "x9ja".
The variable y is assigned "x9ja".
The assertion checks the value of y.
[/THOUGHT]
[ANSWER]
assert(y == "x9ja")
[/ANSWER]
"""


USER_PROMPT_TMPL_NO_COT = """
[PYTHON]
{code}
[/PYTHON]
[ANSWER]
"""


USER_PROMPT_TMPL_COT = """
[PYTHON]
{code}
[/PYTHON]
[THOUGHT]
"""

```

### remove_empty_output.py

```
import json

# 输入和输出文件路径
input_file = r'result\Qwen3-235B-A22B-Thinking-2507_thought.jsonl'
output_file = r'result\Qwen3-235B-A22B-Thinking-2507_thought_cleaned.jsonl'

# 读取文件，删除 raw_output 为空的数据，写入新文件
deleted_count = 0
kept_count = 0

with open(input_file, 'r', encoding='utf-8') as infile, \
     open(output_file, 'w', encoding='utf-8') as outfile:
    for line in infile:
        if line.strip():  # 跳过空行
            data = json.loads(line)
            # 检查 raw_output 是否为空
            raw_output = data.get('raw_output', '')
            if raw_output and raw_output.strip():  # 如果 raw_output 不为空
                outfile.write(json.dumps(data, ensure_ascii=False) + '\n')
                kept_count += 1
            else:
                deleted_count += 1

print(f"✓ 完成！")
print(f"✓ 删除了 {deleted_count} 条 raw_output 为空的数据")
print(f"✓ 保留了 {kept_count} 条数据")
print(f"✓ 结果已保存到 {output_file}")

```

### stastic_function_call_precision.py

```
import json
import re
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
import os

# ======================
# 统计函数调用次数
# ======================
def count_function_calls(code: str) -> int:
    def_pattern = r'^\s*def\s+(\w+)\s*\('
    lines = code.split("\n")

    function_names = set()
    for line in lines:
        m = re.match(def_pattern, line)
        if m:
            function_names.add(m.group(1))

    call_count = 0
    for line in lines:
        for name in function_names:
            if f"{name}(" in line and not re.match(rf'^\s*def\s+{name}', line):
                call_count += line.count(f"{name}(")

    return call_count


# Bucketing for plotting: [1, 2-3, 4-6, 7-10, 10+]
BUCKET_LABELS = ["1", "2-3", "4-6", "7-10", "10+"]

def map_count_to_bucket(count: int):
    if count <= 0:
        return None
    if count == 1:
        return "1"
    if 2 <= count <= 3:
        return "2-3"
    if 4 <= count <= 6:
        return "4-6"
    if 7 <= count <= 10:
        return "7-10"
    # count >= 11
    return "10+"


# ======================
# 单模型分析（保留原功能）
# ======================
def analyze_accuracy_vs_function_calls(
    dataset_file: str,
    result_file: str,
    return_stats: bool = False,
):
    code_map = {}
    with open(dataset_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                obj = json.loads(line)
                code_map[obj["id"]] = obj.get("task", {}).get("code", "")

    result_map = {}
    with open(result_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                obj = json.loads(line)
                result_map[obj["id"]] = bool(obj.get("correct", False))

    stats = defaultdict(lambda: {"correct": 0, "total": 0})
    missing = 0

    for id_, code in code_map.items():
        if id_ not in result_map:
            missing += 1
            continue

        call_count = count_function_calls(code)
        bucket = map_count_to_bucket(call_count)
        if bucket is None:
            # skip samples with zero function calls for this bucketed plot
            continue

        is_correct = result_map[id_]

        stats[bucket]["total"] += 1
        if is_correct:
            stats[bucket]["correct"] += 1

    # Use the fixed bucket order for plotting
    call_counts = [b for b in BUCKET_LABELS if b in stats]
    accuracies = [stats[c]["correct"] / stats[c]["total"] for c in call_counts]

    # ===== 单模型画图 =====
    result_name = os.path.basename(result_file).replace(".jsonl", "")
    plt.figure(figsize=(7, 5))
    plt.plot(call_counts, accuracies, marker="o", linewidth=2)

    plt.xlabel("Function Call Bucket")
    plt.ylabel("Accuracy")
    plt.title(f"Accuracy vs. Function Call Bucket ({result_name})")

    plt.ylim(0, 1.05)
    plt.grid(True, linestyle="--", alpha=0.5)

    # Plot on integer x positions and label ticks with bucket labels
    x = list(range(len(call_counts)))
    plt.clf()
    plt.figure(figsize=(7, 5))
    plt.plot(x, accuracies, marker="o", linewidth=2)
    plt.xlabel("Function Call Bucket")
    plt.ylabel("Accuracy")
    plt.title(f"Accuracy vs. Function Call Bucket ({result_name})")
    plt.ylim(0, 1.05)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.xticks(x, call_counts)
    for xi, yi in zip(x, accuracies):
        plt.text(xi, yi + 0.03, f"{yi:.2f}", ha="center", fontsize=9)

    os.makedirs("./pictures", exist_ok=True)
    plt.tight_layout()
    plt.savefig(f"./pictures/accuracy_vs_function_calls_{result_name}.png", dpi=300)
    plt.close()

    print(f"✓ Saved figure: accuracy_vs_function_calls_{result_name}.png")
    print(f"✓ Matched samples: {sum(v['total'] for v in stats.values())}")
    print(f"⚠ Missing results: {missing}")

    if return_stats:
        return stats


# ======================
# 多模型平均分析（新增）
# ======================
def analyze_average_accuracy_vs_function_calls(
    dataset_file: str,
    result_files: list,
):
    all_model_stats = []

    for rf in result_files:
        stats = analyze_accuracy_vs_function_calls(
            dataset_file,
            rf,
            return_stats=True
        )
        all_model_stats.append(stats)

    # Use fixed bucket order and compute average accuracy per bucket
    all_call_counts = [b for b in BUCKET_LABELS if any((b in stats and stats[b]["total"] > 0) for stats in all_model_stats)]

    avg_accuracies = []
    for c in all_call_counts:
        accs = []
        for stats in all_model_stats:
            if c in stats and stats[c]["total"] > 0:
                accs.append(stats[c]["correct"] / stats[c]["total"])
        avg_accuracies.append(np.mean(accs) if accs else 0.0)

    # ===== 平均准确率画图 =====
    # Plot using integer x positions and label ticks with bucket labels
    x = list(range(len(all_call_counts)))
    plt.figure(figsize=(7, 5))
    plt.plot(x, avg_accuracies, marker="o", linewidth=2, color="black")

    plt.xlabel("Function Call Bucket")
    plt.ylabel("Average Accuracy")
    plt.title("Average Accuracy vs. Function Call Bucket (All Models)")

    plt.ylim(0, 1.05)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.xticks(x, all_call_counts)

    for xi, yi in zip(x, avg_accuracies):
        plt.text(xi, yi + 0.03, f"{yi:.2f}", ha="center", fontsize=9)

    os.makedirs("./pictures", exist_ok=True)
    plt.tight_layout()
    plt.savefig("./pictures/accuracy_vs_function_calls_average.png", dpi=300)
    plt.close()

    print("✓ Saved figure: accuracy_vs_function_calls_average.png")


# ======================
# 入口
# ======================
if __name__ == "__main__":
    dataset_file = "./data/Qwen3-32B_vs_Qwen3-14B_size500.jsonl"
    result_files = [
        "./result/Qwen3-32B_thought.jsonl",
        "./result/Qwen3-14B_thought.jsonl",
        "./result/Qwen3-8B_thought.jsonl",
        "./result/Qwen3-Coder-30B-A3B-Instruct_thought.jsonl",
        "./result/deepseek-coder-33b-instruct_thought.jsonl",
        "./result/QwQ-32B_thought.jsonl"
    ]

    # 分别统计（原行为）
    for rf in result_files:
        analyze_accuracy_vs_function_calls(dataset_file, rf)

    # ===== 是否统计平均 =====
    AVERAGE = True
    if AVERAGE:
        analyze_average_accuracy_vs_function_calls(
            dataset_file,
            result_files
        )

```

### run_all_experiments.py

```
#!/usr/bin/env python3
"""
run_all_experiments.py
FuncCodeBench 主评估实验 — 并行运行所有 API 模型（cot / ncot 双路）

用法:
    python run_all_experiments.py                                      # 全部模型 × both（默认 8 并发）
    python run_all_experiments.py --mode cot                           # 只跑 cot
    python run_all_experiments.py --mode ncot                          # 只跑 ncot
    python run_all_experiments.py --workers 12                         # 指定并发数
    python run_all_experiments.py --dry-run                            # 仅打印命令，不执行
    python run_all_experiments.py --skip-done                          # 跳过已有完整结果的 case
    python run_all_experiments.py --only gpt-4o,gpt-5,grok-2          # 只运行指定模型（逗号分隔）

跑 6 个模型的 12 个 case:
    python run_all_experiments.py \
        --only gpt-4o,gpt-4.1-mini,o1,gpt-5,grok-2,grok-3-mini-beta \
        --workers 12
"""

import argparse
import logging
import subprocess
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

# ==============================================================
# 日志配置
# ==============================================================
_ts = datetime.now().strftime("%Y%m%d_%H%M%S")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(f"run_all_{_ts}.log", encoding="utf-8"),
    ],
)
logger = logging.getLogger(__name__)
_print_lock = threading.Lock()

# ==============================================================
# 路径
# cot  结果 → result-cot/
# ncot 结果 → result-ncot/
# ==============================================================
SCRIPT_DIR      = Path(__file__).parent
INPUT_FILE      = SCRIPT_DIR / "data" / "cross_function_with_assert.jsonl"
RESULT_COT_DIR  = SCRIPT_DIR / "result-cot"
RESULT_NCOT_DIR = SCRIPT_DIR / "result-ncot"

for _d in (RESULT_COT_DIR, RESULT_NCOT_DIR):
    _d.mkdir(exist_ok=True)

# ==============================================================
# API 密钥 & Endpoint
# ==============================================================
PARATERA_KEY    = "sk-0ABx5wpLhRLL-ZKEwiKY_w"
PARATERA_URL    = "https://llmapi.paratera.com/v1/"

EZAI_URL        = "https://api.ezai88.com/v1"
EZAI_GPT_KEY    = "sk-NdltMkcERI1Klsyjo4Trzo1sKph6blaaFo0vulEjizV4g8ts"
EZAI_GEMINI_KEY = "sk-C28dDH1FD2RPrzNzhSVd1brwUJNWgdcCcccEJZglCdWob2kj"
EZAI_CLAUDE_KEY = "sk-gq8qRNNiNIjS0x8tzfMl8F9bscL4wopT7oA2qD2FU8xKTrnp"

# ==============================================================
# 推理通用参数
# ==============================================================
TEMPERATURE    = 0
MAX_NEW_TOKENS = 2048
BATCH_SIZE     = 4

# ==============================================================
# 模型列表
# 注意：不再含 "cot" 字段，由 build_tasks() 自动展开为 cot / ncot 两个 task
# ==============================================================
MODELS = [
    # ──────────────────── Paratera: Qwen3 系列 ────────────────────
    {
        "api_model": "Qwen3-Next-80B-A3B-Instruct",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": False, "output_name": "Qwen3-Next-80B-Instruct",
    },
    {
        "api_model": "Qwen3-235B-A22B-Instruct-2507",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": False, "output_name": "Qwen3-235B-Instruct",
    },
    {
        "api_model": "Qwen3-32B",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "Qwen2.5-72B-Instruct",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": False, "output_name": None,
    },

    # ──────────────────── Paratera: DeepSeek 系列 ─────────────────
    {
        "api_model": "DeepSeek-V3.2",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "DeepSeek-V3.2-Thinking",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": True, "output_name": None,
    },
    {
        "api_model": "DeepSeek-V3.1",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "DeepSeek-R1",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": True, "output_name": None,
    },

    # ──────────────────── Paratera: Kimi ──────────────────────────
    {
        "api_model": "Kimi-K2",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": False, "output_name": None,
    },

    # ──────────────────── Paratera: GLM 系列 ──────────────────────
    {
        "api_model": "GLM-4.6",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "GLM-4.5",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "GLM-5",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "GLM-4-Flash",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": False, "output_name": None,
    },

    # ──────────────────── Paratera: MiniMax 系列 ──────────────────
    {
        "api_model": "MiniMax-M1-80k",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "MiniMax-M2",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "MiniMax-M2.5",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": False, "output_name": None,
    },

    # ──────────────────── Paratera: Coder 系列 ────────────────────
    {
        "api_model": "Qwen3-Coder-480B-A35B-Instruct",
        "base_url": PARATERA_URL, "api_key": PARATERA_KEY,
        "enable_thinking": False, "output_name": None,
    },

    # ──────────────────── EzAI: GPT 系列 ──────────────────────────
    {
        "api_model": "gpt-3.5-turbo",
        "base_url": EZAI_URL, "api_key": EZAI_GPT_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "gpt-4",
        "base_url": EZAI_URL, "api_key": EZAI_GPT_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "gpt-4o",
        "base_url": EZAI_URL, "api_key": EZAI_GPT_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "gpt-4.1-mini",
        "base_url": EZAI_URL, "api_key": EZAI_GPT_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "o1",
        "base_url": EZAI_URL, "api_key": EZAI_GPT_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "gpt-5",
        "base_url": EZAI_URL, "api_key": EZAI_GPT_KEY,
        "enable_thinking": False, "output_name": None,
    },

    # ──────────────────── EzAI: Grok 系列 ─────────────────────────
    {
        "api_model": "grok-2",
        "base_url": EZAI_URL, "api_key": EZAI_GPT_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "grok-3-mini-beta",
        "base_url": EZAI_URL, "api_key": EZAI_GPT_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "grok-4",
        "base_url": EZAI_URL, "api_key": EZAI_GPT_KEY,
        "enable_thinking": False, "output_name": None,
    },

    # ──────────────────── EzAI: Gemini 系列 ───────────────────────
    {
        "api_model": "gemini-2.0-flash",
        "base_url": EZAI_URL, "api_key": EZAI_GEMINI_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "gemini-2.5-flash",
        "base_url": EZAI_URL, "api_key": EZAI_GEMINI_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "gemini-2.5-pro",
        "base_url": EZAI_URL, "api_key": EZAI_GEMINI_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "gemini-3-flash-preview",
        "base_url": EZAI_URL, "api_key": EZAI_GEMINI_KEY,
        "enable_thinking": False, "output_name": None,
    },

    # ──────────────────── EzAI: Claude 系列 ───────────────────────
    {
        "api_model": "claude-3-7-sonnet-20250219",
        "base_url": EZAI_URL, "api_key": EZAI_CLAUDE_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "claude-sonnet-4-20250514",
        "base_url": EZAI_URL, "api_key": EZAI_CLAUDE_KEY,
        "enable_thinking": False, "output_name": None,
    },
    {
        "api_model": "claude-sonnet-4-5-20250929",
        "base_url": EZAI_URL, "api_key": EZAI_CLAUDE_KEY,
        "enable_thinking": False, "output_name": None,
    },
]


# ==============================================================
# 工具函数
# ==============================================================

def count_jsonl_lines(path: Path) -> int:
    if not path.exists():
        return 0
    count = 0
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                count += 1
    return count


def result_dir(cot: bool) -> Path:
    """根据 cot 标志返回对应的结果目录。"""
    return RESULT_COT_DIR if cot else RESULT_NCOT_DIR


def get_output_path(task: dict) -> Path:
    name = task.get("output_name") or task["api_model"]
    return result_dir(task["cot"]) / f"{name}.jsonl"


def get_log_path(task: dict) -> Path:
    name = task.get("output_name") or task["api_model"]
    return result_dir(task["cot"]) / f"{name}_analysis.log"


def get_proc_log_path(task: dict) -> Path:
    name = task.get("output_name") or task["api_model"]
    return result_dir(task["cot"]) / f"{name}_proc.log"


def task_label(task: dict) -> str:
    """用于日志的任务标签，含 [cot] / [ncot] 后缀。"""
    name = task.get("output_name") or task["api_model"]
    return f"{name}[{'cot' if task['cot'] else 'ncot'}]"


def build_tasks(models: list[dict], mode: str) -> list[dict]:
    """
    将模型列表按 mode 展开为 task 列表。
      both → 每个模型生成 ncot + cot 两个 task
      cot  → 只生成 cot task
      ncot → 只生成 ncot task
    """
    cot_flags: list[bool] = {
        "both": [False, True],
        "cot":  [True],
        "ncot": [False],
    }[mode]

    tasks = []
    for cfg in models:
        for cot in cot_flags:
            task = {k: v for k, v in cfg.items() if k != "cot"}  # 丢弃旧 cot 字段（如有）
            task["cot"] = cot
            tasks.append(task)
    return tasks


# ==============================================================
# 单任务运行逻辑（在线程池中被调用）
# ==============================================================

def run_task(task: dict, dry_run: bool = False) -> tuple[str, bool]:
    """
    运行单个 task 的 eval_runner + analyze_results。
    返回 (task_label, success)。
    此函数在子线程中执行，所有输出写文件，不直接打印到终端。
    """
    label       = task_label(task)
    output_file = get_output_path(task)
    log_file    = get_log_path(task)
    proc_log    = get_proc_log_path(task)

    with _print_lock:
        logger.info("▶ START [%s]  →  %s", label, output_file)

    # ── Step 1: eval_runner ──────────────────────────────────────
    eval_cmd = [
        sys.executable,
        str(SCRIPT_DIR / "eval_runner.py"),
        "--backend",        "api",
        "--input",          str(INPUT_FILE),
        "--output",         str(output_file),
        "--api_base_url",   task["base_url"],
        "--api_model",      task["api_model"],
        "--api_key",        task["api_key"],
        "--temperature",    str(TEMPERATURE),
        "--max_new_tokens", str(MAX_NEW_TOKENS),
        "--batch_size",     str(BATCH_SIZE),
        "--resume",
    ]
    if task.get("enable_thinking"):
        eval_cmd.append("--enable_thinking")
    if task["cot"]:
        eval_cmd.append("--cot")

    with _print_lock:
        logger.info("CMD [%s]: %s", label, " ".join(eval_cmd))

    if not dry_run:
        with proc_log.open("w", encoding="utf-8") as pf:
            ret = subprocess.run(eval_cmd, cwd=str(SCRIPT_DIR), stdout=pf, stderr=pf)

        if ret.returncode != 0:
            with _print_lock:
                logger.error(
                    "❌ FAILED [%s]  code=%d  详情见: %s",
                    label, ret.returncode, proc_log,
                )
            return label, False

    # ── Step 2: analyze_results ──────────────────────────────────
    analyze_cmd = [
        sys.executable,
        str(SCRIPT_DIR / "analyze_results.py"),
        str(output_file),
    ]

    if not dry_run:
        with log_file.open("w", encoding="utf-8") as lf:
            subprocess.run(analyze_cmd, stdout=lf, stderr=lf, cwd=str(SCRIPT_DIR))

    with _print_lock:
        logger.info("✅ DONE  [%s]", label)

    return label, True


# ==============================================================
# 主流程
# ==============================================================

def main():
    ap = argparse.ArgumentParser(
        description="FuncCodeBench 主评估实验并行运行器（cot/ncot 双路）"
    )
    ap.add_argument(
        "--mode", choices=["both", "cot", "ncot"], default="both",
        help="运行模式：both=cot+ncot（默认），cot=仅cot，ncot=仅ncot",
    )
    ap.add_argument(
        "--workers", type=int, default=8,
        help="最大并发 task 数（默认 8）",
    )
    ap.add_argument("--dry-run",   action="store_true", help="只打印命令，不实际执行")
    ap.add_argument("--skip-done", action="store_true", help="结果文件行数 ≥ 数据集行数时自动跳过")
    ap.add_argument(
        "--only", type=str, default=None,
        help="逗号分隔的模型名（api_model 或 output_name），只运行这些模型",
    )
    args = ap.parse_args()

    total_samples = count_jsonl_lines(INPUT_FILE)
    logger.info("数据集: %s  |  总样本数: %d", INPUT_FILE, total_samples)
    logger.info("结果目录: result-cot/  &  result-ncot/")
    logger.info("运行模式: %s  |  并发数: %d", args.mode, args.workers)

    # ── 模型过滤（--only） ─────────────────────────────────────────
    models = MODELS
    if args.only:
        only_set = set(args.only.split(","))
        models = [
            m for m in MODELS
            if m["api_model"] in only_set
            or (m.get("output_name") or "") in only_set
        ]
        logger.info("按 --only 筛选后，共 %d 个模型", len(models))

    # ── 展开为 tasks ──────────────────────────────────────────────
    all_tasks = build_tasks(models, args.mode)
    logger.info("总 task 数: %d", len(all_tasks))

    # ── skip-done 预筛选 ──────────────────────────────────────────
    to_run:       list[dict] = []
    skipped_list: list[str]  = []

    for task in all_tasks:
        label        = task_label(task)
        output_file  = get_output_path(task)
        existing_cnt = count_jsonl_lines(output_file)

        logger.info("%-55s | 已有 %d / %d 条", label, existing_cnt, total_samples)

        if args.skip_done and existing_cnt >= total_samples:
            logger.info("⏭  已完整，跳过: %s", label)
            skipped_list.append(label)
        else:
            to_run.append(task)

    logger.info("=" * 60)
    logger.info("待运行 tasks: %d  |  并发数: %d", len(to_run), args.workers)
    logger.info("=" * 60)

    success_list: list[str] = []
    failed_list:  list[str] = []

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {
            pool.submit(run_task, task, args.dry_run): task
            for task in to_run
        }

        for future in as_completed(futures):
            task = futures[future]
            try:
                label, ok = future.result()
            except Exception as exc:
                label = task_label(task)
                logger.exception("💥 未捕获异常 [%s]: %s", label, exc)
                ok = False

            (success_list if ok else failed_list).append(label)

    # ── 汇总 ──────────────────────────────────────────────────────
    logger.info("=" * 60)
    logger.info(
        "汇总  总 task=%d  成功=%d  跳过=%d  失败=%d",
        len(all_tasks), len(success_list), len(skipped_list), len(failed_list),
    )
    if success_list:
        logger.info("✅ 成功: %s", ", ".join(sorted(success_list)))
    if skipped_list:
        logger.info("⏭  跳过: %s", ", ".join(skipped_list))
    if failed_list:
        logger.error("❌ 失败: %s", ", ".join(sorted(failed_list)))
        logger.error("失败 task 的详细日志在对应 result-*/..._proc.log 中")


if __name__ == "__main__":
    main()
```

