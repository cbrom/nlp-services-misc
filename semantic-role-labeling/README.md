# allen-srl
![singnetlogo](../docs/assets/singnet-logo.jpg?raw=true 'SingularityNET')

Semantic Role Labeling
======================
Definition and Application area
----------
Semantic Role Labeling (SRL) recovers the latent predicate argument structure of a sentence, providing representations that answer basic questions about sentence meaning, including “who” did “what” to “whom,” etc.

This service provides a wrapper around [allenlp](https://demo.allennlp.org/semantic-role-labeling)'s great demo and models available for semantic role labeling

Installation 
============
* Natively
```bash
pip install -r requirements.txt
./install.sh
```
* Using Docker
```bash
docker build -t singuliartynet/semantic-role-labeling-service .
```

Deployment
-----
- GRPC endpoint
```
docker run --rm -it -p 8001 --name coref singularitynet/semantic-role-labeling-service 
```
- Dameon endpoint
```
docker run --rm -it -p 8007 -p 8008 --name coref singularitynet/semantic-role-labeling-service
```

For sample usage: Look at [usage](../../docs/users_guide/index.html) documentation.

Authors
------
- Zelalem Fantahun - Author - [SingularityNet.io](https://singularitynet.io)
- Kbrom Abadi - Author
- Tesfa Yohannes - Maintainer - [SingularityNet.io](https://singularitynet.io)