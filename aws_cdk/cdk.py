from aws_cdk import (
    aws_eks as eks,
    aws_ec2 as ec2,
    core
)

class EKSClusterStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # VPC 생성 (2개 AZ)
        vpc = ec2.Vpc(self, "MyVPC", max_azs=2)

        # EKS 클러스터 생성
        cluster = eks.Cluster(self, "MyEKSCluster",
            vpc=vpc,
            default_capacity=2,  # 기본 노드 수
            default_capacity_instance=ec2.InstanceType("t3.medium")  # EC2 인스턴스 유형
        )

        # EKS 클러스터의 kubeconfig 파일 업데이트
        cluster.add_auto_scaling_group_capacity(
            instance_type=ec2.InstanceType("t3.medium"),
            min_capacity=2
        )

        # 클러스터 정보 출력 (optional)
        core.CfnOutput(self, "ClusterName", value=cluster.cluster_name)
        core.CfnOutput(self, "ClusterEndpoint", value=cluster.cluster_endpoint)

app = core.App()
EKSClusterStack(app, "EKSClusterStack")
app.synth()
