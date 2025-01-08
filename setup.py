from setuptools import setup, find_packages

setup(
    name="ggfm",  # package name
    version="0.1",
    packages=find_packages(),
    install_requires=['absl-py==2.0.0', 'accelerate==0.25.0', 
                      'aiofiles==23.2.1', 'aiohttp==3.8.4', 
                      'aiosignal==1.3.1', 'alabaster==0.7.13', 
                      'alembic==1.13.1', 'altair==5.2.0', 
                      'anyio==3.7.1', 'appdirs==1.4.4', 
                      'arxiv==2.1.0', 'astunparse==1.6.3', 
                      'async-timeout==4.0.3', 'attrs==23.1.0', 
                      'autopep8==2.0.4', 'Babel==2.14.0', 
                      'banal==1.0.6', 'cachetools==5.3.2', 
                      'certifi==2023.11.17', 'charset-normalizer==3.3.2', 
                      'click==8.1.7', 'conda-pack==0.7.1', 
                      'contourpy==1.1.1', 'cycler==0.12.1', 
                      'Cython==3.0.11', 'dataset==1.6.2', 
                      'datasets==2.17.1', 'dgl==2.0.0+cu121', 
                      'dglgo==0.0.2', 'dill==0.3.8', 
                      'docker-pycreds==0.4.0', 'docutils==0.20.1', 
                      'einops==0.7.0', 'evaluate==0.4.3', 
                      'exceptiongroup==1.2.0', 
                    #   'fastapi==0.104.1', 
                      'fastapi', 
                      'feedparser==6.0.10', 'ffmpy==0.3.1', 
                      'filelock==3.13.1', 
                    #   'flash-attn==1.0.9', 
                      'flatbuffers==24.3.25', 'fonttools==4.46.0', 
                      'frozenlist==1.4.0', 'fschat==0.2.33', 
                      'fsspec==2023.10.0', 'ftfy==6.1.3', 
                      'gast==0.4.0', 'gensim==4.3.3', 
                      'gitdb==4.0.11', 'GitPython==3.1.40', 
                      'google-auth==2.25.1', 'google-auth-oauthlib==1.0.0', 
                      'google-pasta==0.2.0', 'gradio==3.50.2', 
                      'gradio_client==0.6.1', 'greenlet==3.0.3', 
                      'grpcio==1.60.0', 'h11==0.14.0', 
                      'h5py==3.11.0', 'httpcore==1.0.2', 
                      'httpx==0.25.2', 'huggingface-hub==0.27.0', 
                      'idna==3.6', 'imagesize==1.4.1', 
                      'importlib-metadata==7.0.0', 'importlib-resources==6.1.1', 
                      'isort==5.13.2', 'Jinja2==3.1.2', 
                      'joblib==1.3.2', 'jsonschema==4.20.0', 
                      'jsonschema-specifications==2023.11.2', 'keras==2.13.1', 
                      'kiwisolver==1.4.5', 'libclang==18.1.1', 
                      'lightning-utilities==0.11.2', 'littleutils==0.2.2', 
                      'Mako==1.3.2', 'Markdown==3.5.1', 
                      'markdown-it-py==3.0.0', 'markdown2==2.4.11', 
                      'MarkupSafe==2.1.3', 'matplotlib==3.7.4', 
                      'mdurl==0.1.2', 'modelscope==1.21.1', 
                      'mpmath==1.3.0', 'msgpack==1.0.7', 
                      'multidict==6.0.4', 'multiprocess==0.70.16', 
                      'networkx==3.0', 'nh3==0.2.15', 
                      'ninja==1.11.1.1', 'nltk==3.8.1', 
                      'numpy==1.24.3', 'numpydoc==1.6.0', 
                      'nvidia-cublas-cu12==12.1.3.1', 'nvidia-cuda-cupti-cu12==12.1.105', 
                      'nvidia-cuda-nvrtc-cu12==12.1.105', 'nvidia-cuda-runtime-cu12==12.1.105', 
                      'nvidia-cudnn-cu12==8.9.2.26', 'nvidia-cufft-cu12==11.0.2.54', 
                      'nvidia-curand-cu12==10.3.2.106', 'nvidia-cusolver-cu12==11.4.5.107', 
                      'nvidia-cusparse-cu12==12.1.0.106', 'nvidia-nccl-cu12==2.18.1', 
                      'nvidia-nvjitlink-cu12==12.6.77', 'nvidia-nvtx-cu12==12.1.105', 
                      'oauthlib==3.2.2', 'ogb==1.3.6', 
                      'opt-einsum==3.3.0', 'orjson==3.9.10', 
                      'outdated==0.2.2', 'packaging==23.2', 
                      'pandas==2.0.3', 'peft==0.7.0', 'Pillow==10.1.0', 
                      'pkgutil_resolve_name==1.3.10', 'prompt-toolkit==3.0.41', 
                      'protobuf==4.25.3', 'psutil==5.9.6', 'pyarrow==15.0.0', 
                      'pyarrow-hotfix==0.6', 'pyasn1==0.5.1', 'pyasn1-modules==0.3.0', 
                      'pycairo==1.25.1', 'pycodestyle==2.11.1', 'pydantic==1.10.13', 
                      'pydub==0.25.1', 'pyg-lib==0.3.1+pt21cu121', 'Pygments==2.17.2', 
                      'PyGObject==3.46.0', 'PyMySQL==1.1.1', 'pyparsing==3.1.1', 
                      'python-dateutil==2.8.2', 'python-multipart==0.0.6', 
                      'pytz==2023.3.post1', 'PyYAML==6.0.1', 'ray==2.8.1', 
                      'rdkit-pypi==2022.9.5', 'referencing==0.32.0', 'regex==2023.10.3', 
                      'requests==2.31.0', 'requests-oauthlib==1.3.1', 'rich==13.7.0', 
                      'rpds-py==0.13.2', 'rsa==4.9', 'ruamel.yaml==0.18.6', 
                      'ruamel.yaml.clib==0.2.8', 'safetensors==0.4.1', 
                      'scikit-learn==1.3.2', 'scipy==1.10.1', 'seaborn==0.13.2', 
                      'semantic-version==2.10.0', 'sentencepiece==0.1.99', 
                      'sentry-sdk==1.38.0', 'setproctitle==1.3.3', 
                      'sgmllib3k==1.0.0', 'shortuuid==1.0.11', 'six==1.16.0', 
                      'smart-open==7.0.5', 'smmap==5.0.1', 'sniffio==1.3.0', 
                      'snowballstemmer==2.2.0', 'Sphinx==7.1.2', 
                      'sphinxcontrib-applehelp==1.0.4', 'sphinxcontrib-devhelp==1.0.2', 
                      'sphinxcontrib-htmlhelp==2.0.1', 'sphinxcontrib-jsmath==1.0.1', 
                      'sphinxcontrib-qthelp==1.0.3', 'sphinxcontrib-serializinghtml==1.1.5', 
                      'SQLAlchemy==1.4.51', 'starlette==0.27.0', 'svgwrite==1.4.3', 
                      'sympy==1.12', 'tabulate==0.9.0', 'tensorboard==2.13.0', 
                      'tensorboard-data-server==0.7.2', 'tensorflow==2.13.1', 
                      'tensorflow-estimator==2.13.0', 'tensorflow-io-gcs-filesystem==0.34.0', 
                      'termcolor==2.4.0', 'texttable==1.7.0', 'threadpoolctl==3.2.0', 
                      'tiktoken==0.5.2', 'tokenizers==0.20.3', 'tomli==2.0.1', 
                      'toolz==0.12.0', 'torch==2.1.0', 'torch-cluster==1.6.3+pt21cu121', 
                      'torch-scatter==2.1.2+pt21cu121', 'torch-sparse==0.6.18+pt21cu121', 
                      'torch-spline-conv==1.2.2+pt21cu121', 'torch_geometric==2.4.0', 
                      'torchaudio==2.1.0+cu121', 'torchdata==0.7.1', 'torchmetrics==1.3.2', 
                      'torchvision==0.16.0+cu121', 'tqdm==4.66.1', 'transformers==4.46.3', 
                      'triton==2.1.0', 'typer==0.9.0', 
                    #   'typing_extensions==4.5.0', 
                      'tzdata==2023.3', 'urllib3==2.1.0', 'uvicorn==0.24.0.post1', 
                      'wandb==0.16.1', 'wavedrom==2.0.3.post3', 'wcwidth==0.2.12', 
                      'websockets==11.0.3', 'Werkzeug==3.0.1', 'wrapt==1.16.0', 
                      'xxhash==3.4.1', 'yarl==1.9.4', 'zipp==3.17.0'],
)
