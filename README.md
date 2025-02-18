## New Project in Docker

the process i did was as 
```bash
mkdir docker_jenkins
cd docker_jenkins

git init
mkdir doc_app
touch doc_app/app.py doc_app/routes.py doc_app/models.py doc_app/requirements.txt
```
Write down the code then
* For Jenkins (Download Oracle JDK 21 or 17) I had 23 

```ps
docker-compose up --build
```
