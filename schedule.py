import numpy as np


class Schedule:
    """ Schedule 课程类.

    描述:
        包含了课程、班级、教师、教室、星期、时间几个属性
        其中前三个是我们自定义的，后三个是需要算法来优化
    """
    def __init__(self, classId, courseId, teacherId):
        """Init
        参数:
            courseId:  int, 课程ID.
            classId:   int, 班级ID.
            teacherId: int, 教师ID.
        """
        self.courseId = courseId
        self.classId = classId
        self.teacherId = teacherId

        # 教室ID
        self.roomId = 0
        # 星期
        self.weekDay = 0
        # 时间
        self.slot = 0

    def random_init(self, roomRange):
        """ 随机初始化

        参数:
            roomSize: int, 教室数量.
        """
        self.roomId = np.random.randint(1, roomRange + 1, 1)[0]
        self.weekDay = np.random.randint(1, 6, 1)[0]
        self.slot = np.random.randint(1, 6, 1)[0]

def schedule_cost(population, elite):
    """ 计算课表种群的冲突

    描述:
        冲突检测遵循下面几条规则：
            同一个教室在同一个时间只能有一门课。
            同一个班级在同一个时间只能有一门课 。
            同一个教师在同一个时间只能有一门课。
            同一个班级在同一天不能有相同的课。

    参数:
        population: List, 上课时间表. { 种群（Population）}
        elite:      int,  最好的结果数（需要挑选出的最优个体数量）.

    返回:
        1: 挑选出最优的N(elite)个个体
        2: 最优个体的适应度
    """

    # 冲突数量（种群舒适度）
    conflicts = []
    # 种群数量
    populationLen = len(population[0])

    # 计算种群冲突()
    for p in population:
        conflict = 0
        for i in range(0, populationLen - 1):
            for j in range(i + 1, populationLen):
                # check course in same time and same room 
                if p[i].roomId == p[j].roomId and p[i].weekDay == p[j].weekDay and p[i].slot == p[j].slot:
                    conflict += 1
                # check course for one class in same time
                if p[i].classId == p[j].classId and p[i].weekDay == p[j].weekDay and p[i].slot == p[j].slot:
                    conflict += 1
                # check course for one teacher in same time
                if p[i].teacherId == p[j].teacherId and p[i].weekDay == p[j].weekDay and p[i].slot == p[j].slot:
                    conflict += 1
                # check same course for one class in same day
                if p[i].classId == p[j].classId and p[i].courseId == p[j].courseId and p[i].weekDay == p[j].weekDay:
                    conflict += 1
        # 存储冲突数量(种群适应度)
        conflicts.append(conflict)

    # 根据适应度对种群排序
    index = np.array(conflicts).argsort()

    # 返回值
    return index[: elite], conflicts[index[0]]