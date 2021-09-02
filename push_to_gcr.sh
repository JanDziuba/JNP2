docker build -t gcr.io/totodom/front ./front
docker push gcr.io/totodom/front

docker build -t gcr.io/totodom/users ./users
docker push gcr.io/totodom/users

docker build -t gcr.io/totodom/offers ./offers
docker push gcr.io/totodom/offers

docker build -t gcr.io/totodom/chat ./chat
docker push gcr.io/totodom/chat