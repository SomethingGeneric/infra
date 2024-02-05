# Deploy steps
1. Run playbook
2. Reboot each node
3. `kubeadm init --pod-network-cidr=192.168.40.0/16` on master
4. Deploy flannel
5. `kubeadm join ...` on workers
6. Profit?