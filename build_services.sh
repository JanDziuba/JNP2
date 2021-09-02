kubectl apply -f https://bit.ly/k4k8s # create Kong API gateway
kubectl apply -f kubernetes/ingress.yml

kubectl apply -f kubernetes/front.yml
kubectl apply -f kubernetes/users.yml
kubectl apply -f kubernetes/offers.yml
