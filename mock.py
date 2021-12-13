import random


class ECSInfo(object):

    def __init__(self, pk, name, tags, ip):
        self.ip = ip
        self.pk = pk
        self.name = name
        self.tags = tags

    def __repr__(self):
        return f'pk:{self.pk}-name:{self.name}'


class Mock(object):

    def __init__(self, max_num):
        self.regain_list = [
            'beijing', 'shanghai', 'hangzhou',
            'tianjin', 'US', 'UA', 'shenzhen'
        ]
        self.type_list = [
            'prod', 'dev', 'test', 'pro-dev'
        ]
        self.group_list = [
            'elk', 'k8s', 'docker', 'server_tree',
            'loki', 'jenkins', 'gitlab', 'rtmp',
            'BR', 'm8_teacher_rtmp_server'
        ]
        self.cluster_list = [
            'ecs', 'rds', 'elb'
        ]
        self.cpu_core = [
            '2u', '4u', '8u', '16u', '32u'
        ]
        self.mem_size = [
            '8G', '32G', '64G', '128G'
        ]

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

    def __init__(self):
        self.eq = 0
        self.ne = 1
        self.rex = 2
        self.nrex = 3
