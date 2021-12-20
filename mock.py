import random


class ECSInfo(object):
    """
    模拟cmdb中资产数据
    """

    def __init__(self, pk, name, tags, ip):
        self.ip = ip
        self.pk = pk
        self.name = name
        self.tags = tags

    def __repr__(self):
        return f'pk:{self.pk}-name:{self.name}'


class Mock(object):
    """
    构建测试用例 调试用
    """

    def __init__(self, max_num):
        # 地区列表
        self.regain_list = [
            'beijing', 'shanghai', 'hangzhou',
            'tianjin', 'US', 'UA', 'shenzhen'
        ]

        # ecs type
        self.type_list = [
            'prod', 'dev', 'test', 'pro-dev'
        ]

        # 组列表
        self.group_list = [
            'elk', 'k8s', 'docker', 'server_tree',
            'loki', 'jenkins', 'gitlab', 'rtmp',
            'BR', 'm8_teacher_rtmp_server'
        ]

        # 集群信息
        self.cluster_list = [
            'ecs', 'rds', 'elb'
        ]

        # cpu 核数
        self.cpu_core = [
            '2', '4', '8', '16', '32'
        ]

        # 内存大小
        self.mem_size = [
            '8', '32', '64', '128'
        ]

        # 本次 mock 的资产数量
        self.mock_objs_num = max_num

    def mock_ecs_objs(self):
        tmp = []
        base_name = 'ecs-{}'
        pk_base_list = list(range(self.mock_objs_num))

        # 打散 pk
        random.shuffle(pk_base_list)

        def get_random_ip():
            return '.'.join([str(random.randint(1, 255)) for _ in range(4)])

        for pk in pk_base_list:
            # mock ecs objs
            ip = get_random_ip()
            hostname = base_name.format(pk)
            tags = {
                'regain': random.choice(self.regain_list),
                'type': random.choice(self.type_list),
                'group': random.choice(self.group_list),
                'cluster': random.choice(self.cluster_list),
                'cpu_core': random.choice(self.cpu_core),
                'mem_size': random.choice(self.mem_size),
            }
            tmp.append(ECSInfo(pk=pk, name=hostname, tags=tags, ip=ip))
        return tmp


class Express(object):
    """
    四种匹配规则类型
    eq   相等
    ne   不相等
    rex  正则匹配
    nrex 正则不匹配
    """

    def __init__(self):
        self.eq = 0
        self.ne = 1
        self.rex = 2
        self.nrex = 3
