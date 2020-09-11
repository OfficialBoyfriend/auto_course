import prettytable 

from schedule import Schedule
from genetic import GeneticOptimize

def vis(schedule):
    """可视化班级课程表

    参数:
        schedule: List, 班级课程表
    """
    col_labels = ['星期/时间', '周一', '周二', '周三', '周四', '周五']
    table_vals = [[i + 1, '', '', '', '', ''] for i in range(5)]

    # 设置表头
    table = prettytable.PrettyTable(col_labels, hrules=prettytable.ALL)

    for s in schedule:
        weekDay = s.weekDay
        slot = s.slot
        text = '{} \n {} \n {} \n {}'.format(s.courseId, s.classId, s.roomId, s.teacherId)
        table_vals[weekDay - 1][slot] = text

    for row in table_vals:
        table.add_row(row)

    print(table)


if __name__ == '__main__':

    # 添加课表
    # (班级, 课程号, 教师号)
    schedules = []

    schedules.append(Schedule(1202, 202, 11102))
    schedules.append(Schedule(1202, 202, 11102))
    schedules.append(Schedule(1202, 202, 11102))
    schedules.append(Schedule(1202, 202, 11102))
    schedules.append(Schedule(1202, 204, 11104))
    schedules.append(Schedule(1202, 204, 11104))
    schedules.append(Schedule(1202, 206, 11106))
    schedules.append(Schedule(1202, 206, 11106))

    schedules.append(Schedule(1203, 203, 11103))
    schedules.append(Schedule(1203, 203, 11103))
    schedules.append(Schedule(1203, 204, 11104))
    schedules.append(Schedule(1203, 204, 11104))
    schedules.append(Schedule(1203, 205, 11105))
    schedules.append(Schedule(1203, 205, 11105))
    schedules.append(Schedule(1203, 206, 11106))
    schedules.append(Schedule(1203, 206, 11106))

    # GA算法优化
    ga = GeneticOptimize(popsize=50, elite=10, maxiter=500)
    res = ga.evolution(schedules, 3)

    # ID与名称映射
    className = {1202: "机器人1802", 1203: "机器人1801"}
    courseName = {202: "幼师英语", 204: "美术", 206:"舞蹈", 203:"钢琴", 205:"声乐"}
    teacherName = {11102:"李宝田", 11104: "宝田李", 11106:"李田保", 11103:"巴拉巴拉", 11105:"啊吧啊吧"}
    roomName = {1:"一教201", 2:"一教202",3:"一教203"}

    # 打印结果表格
    new_dict = {}
    for r in res:
        classId = r.classId
        r.classId = className[classId]
        r.courseId = courseName[r.courseId]
        r.teacherId = teacherName[r.teacherId]
        r.roomId = roomName[r.roomId]
        if classId in new_dict:
            new_dict[classId].append(r)
        else:
            new_dict[classId] = [r]
    for d in new_dict.values():
        vis_res = []
        for value in d:
            vis_res.append(value)
        vis(vis_res)
