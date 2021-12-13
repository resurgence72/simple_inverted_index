import time
from mock import Mock, Express
from inverted_index import InvertIndex

if __name__ == '__main__':
    start = time.time()
    # mock ecs 数据
    invert_index_mock = Mock(max_num=20000)
    ecs_objs = invert_index_mock.mock_ecs_objs()
    print('mock_ecs_objs', time.time() - start)

    ii = InvertIndex()

    # 构建倒排索引
    start = time.time()
    for obj in ecs_objs:
        # 将需要构建的 kv 组合成 dict 类型， 同时需要指定对应的唯一 pk
        tags = obj.tags
        # 将ip 添加
        tags.update({'ip': obj.ip})
        ii.create_invert_index(obj.pk, obj.tags)

    print('create_invert_index', time.time() - start)

    ii.show_invert_index()

    # mock 请求体
    exp = Express()
    req = {
        'labels': [
            {'type': exp.eq, 'key': 'regain', 'value': 'beijing'},
            {'type': exp.ne, 'key': 'type', 'value': 'dev'},
            # {'type': exp.rex, 'key': 'ip', 'value': '.*[456]$'},
        ],
        'target_label': 'group'  # 做统计用，比如将match结果按照 group 维度做分组统计
    }

    start = time.time()
    match_result = ii.find_match_pks_by_labels(
        req.get('labels'),
        req.get('target_label')
    )
    print('find_match_pks_by_labels', time.time() - start)
    print("match_result: ", match_result)
