from durable.lang import *

# AD : 자율주행(Autonomous Driving)

with ruleset('자율주행차운행조건'):
    @when_all(c.first << (m.predicate == 'AD 센서') & (m.object == '문제이면 운행불가.'),
              (m.predicate == '자율차 운행불가 상태') & (m.object == '문제해결 방법이다.') & (m.subject == c.first.subject))
    def Status(c):
        c.assert_fact({ 'subject': c.first.subject, 'predicate': 'AD 센서', 'object': '상태정보를 확인한다.' })

    @when_all((m.predicate == 'AD 센서') & (m.object == '상태정보를 확인한다.'))
    def Lidar(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': 'AD의 Lidar 상태 정보를', 'object': '확인한다.'})
        c.assert_fact({'subject': c.m.subject, 'predicate': 'Lidar 케이블 연결 상태를', 'object': '확인한다.'})

    @when_all((m.predicate == 'AD 센서') & (m.object == '상태정보를 확인한다.'))
    def Radar(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': 'AD의 Radar 상태 정보를', 'object': '확인한다.'})
        c.assert_fact({'subject': c.m.subject, 'predicate': 'Radar 케이블 연결 상태를', 'object': '확인한다.'})

    @when_all((m.predicate == 'AD 센서') & (m.object == '상태정보를 확인한다.'))
    def GPS(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': 'AD의 GPS 상태 정보를', 'object': '확인한다.'})
        c.assert_fact({'subject': c.m.subject, 'predicate': 'GPS 수신감도를', 'object': '확인한다.'})
        c.assert_fact({'subject': c.m.subject, 'predicate': 'GPS 케이블 연결 상태를', 'object': '확인한다.'})

    @when_all(c.first << (m.predicate == '차량 상태') & (m.object == '문제이면 운행불가.'),
              (m.predicate == '차체 운행불가 상태') & (m.object == '문제해결 방법이다.') & (m.subject == c.first.subject))
    def Status(c):
        c.assert_fact({ 'subject': c.first.subject, 'predicate': '차량 상태', 'object': '운핸전 점검 한다.' })

    @when_all((m.predicate == '차량 상태') & (m.object == '운핸전 점검 한다.'))
    def Car(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': '오일 상태를', 'object': '확인한다.'})
        c.assert_fact({'subject': c.m.subject, 'predicate': '소모성 부속품을', 'object': '확인한다.'})

    @when_all((m.predicate == '차량 상태') & (m.object == '운핸전 점검 한다.'))
    def Track(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': '주행 상태를', 'object': '확인한다.'})
        c.assert_fact({'subject': c.m.subject, 'predicate': '전원 상태를', 'object': '확인한다.'})

    @when_all((m.predicate == '차량 상태') & (m.object == '운핸전 점검 한다.'))
    def V2X(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': 'OBU 통신 상태를', 'object': '확인한다.'})
        c.assert_fact({'subject': c.m.subject, 'predicate': 'OBU ANT 수신감도를', 'object': '확인한다.'})        

    @when_all(+m.subject)
    def output(c):
        print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate, c.m.object))

assert_fact('자율주행차운행조건', { 'subject': '자율주행차운행조건', 'predicate': 'AD 센서', 'object': '문제이면 운행불가.' })
assert_fact('자율주행차운행조건', { 'subject': '자율주행차운행조건', 'predicate': '자율차 운행불가 상태', 'object': '문제해결 방법이다.' })
assert_fact('자율주행차운행조건', { 'subject': '자율주행차운행조건', 'predicate': '차량 상태', 'object': '문제이면 운행불가.' })
assert_fact('자율주행차운행조건', { 'subject': '자율주행차운행조건', 'predicate': '차체 운행불가 상태', 'object': '문제해결 방법이다.' })