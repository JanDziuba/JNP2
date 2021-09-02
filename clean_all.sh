# kubectl delete -f https://bit.ly/k4k8s # delete Kong API gateway
kubectl delete ingress ingress

kubectl delete svc front
kubectl delete svc users
kubectl delete svc offers
kubectl delete svc chat
kubectl delete svc redis

kubectl delete deployment front
kubectl delete deployment users
kubectl delete deployment offers
kubectl delete deployment chat
kubectl delete deployment redis