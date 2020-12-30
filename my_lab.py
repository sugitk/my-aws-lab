from diagrams import Cluster, Diagram
from diagrams.aws.network import VPC, VPCPeering
from diagrams.aws.network import NATGateway, InternetGateway
from diagrams.aws.network import PublicSubnet, PrivateSubnet


with Diagram("my lab"):
  with Cluster("ca-central-1"):

    with Cluster("VPC lab") as vpc_lab:

      with Cluster("AZ A (ca-central-1a)"):
        with Cluster("public A (10.0.0.0/25)"):
          public_a = PublicSubnet("public A")
          natgw_a = NATGateway("NAT Gateway A")

        with Cluster("private A (10.0.10.0/25)"):
          private_a = PrivateSubnet("private A")

        private_a >> natgw_a >> public_a

      with Cluster("AZ B (ca-central-1b)"):
        with Cluster("public B (10.0.0.128/25)"):
          public_b = PublicSubnet("public B")
          natgw_b = NATGateway("NAT Gateway B")

        with Cluster("private B (10.0.10.128/25)"):
          private_b = PrivateSubnet("private B")

        private_b >> natgw_b >> public_b

    with Cluster("VPC isolated") as vpc_isolated:
      isolated_a = PublicSubnet("isolated A (192.168.0.0/25)")
      isolated_b = PublicSubnet("isolated B (192.168.0.128/25)")

    peer = VPCPeering("VPC peering gateway")
    [public_a, public_b] - peer - [isolated_a, isolated_b]

    ig = InternetGateway("Internet Gateway")
    [public_a, public_b] >> ig

