class IntComputer:

    def __init__(self, init_commands):
        self.commands = init_commands.copy()
        for i in range(100000):
            self.commands.append(0)
        self.init_val = 0
        self.init_state = False
        self.step = 0

        self.in_val = 0
        self.out_val = 0

        self.relative_base = 0

    def __prepare_comm(self):
        comm = self.commands[self.step]
        temp = "{:05d}".format(comm)
        res = [int(temp[-2:]),
               int(temp[2]),
               int(temp[1]),
               int(temp[0])]
        return res

    def __get_param(self, move, comm):
        param = self.commands[self.step + move]
        if comm[move] == 0:
            res = self.commands[param]
        elif comm[move] == 1:
            res = param
        elif comm[move] == 2:
            res = self.commands[self.relative_base + param]
        return res

    def set_init_val(self, init_val):
        self.init_state = True
        self.init_val = init_val

    def set_input(self, in_val):
        self.in_val = in_val

    def run_program(self):

        while True:
            comm = self.__prepare_comm()

            if comm[0] == 99:
                return "finish"
            elif comm[0] == 1:
                first = self.__get_param(1, comm)
                second = self.__get_param(2, comm)
                pos = self.commands[self.step + 3]
                if comm[3] == 2:
                    pos = pos + self.relative_base
                self.commands[pos] = first + second

                self.step += 4

            elif comm[0] == 2:
                first = self.__get_param(1, comm)
                second = self.__get_param(2, comm)
                pos = self.commands[self.step + 3]
                if comm[3] == 2:
                    pos = pos + self.relative_base
                self.commands[pos] = first * second

                self.step += 4

            elif comm[0] == 3:
                pos = self.commands[self.step + 1]
                if comm[1] == 2:
                    pos = pos + self.relative_base
                self.commands[pos] = self.init_val if self.init_state else self.in_val
                self.init_state = False

                self.step += 2

            elif comm[0] == 4:
                pos = self.__get_param(1, comm)
                self.out_val = pos
                self.step += 2
                print(pos, end=", ")
                return "output"

            elif comm[0] == 5:
                first = self.__get_param(1, comm)
                second = self.__get_param(2, comm)

                if first != 0:
                    self.step = second
                else:
                    self.step += 3

            elif comm[0] == 6:
                first = self.__get_param(1, comm)
                second = self.__get_param(2, comm)

                if first == 0:
                    self.step = second
                else:
                    self.step += 3

            elif comm[0] == 7:
                first = self.__get_param(1, comm)
                second = self.__get_param(2, comm)
                pos = self.commands[self.step + 3]
                if comm[3] == 2:
                    pos = pos + self.relative_base
                self.commands[pos] = 1 if first < second else 0

                self.step += 4

            elif comm[0] == 8:
                first = self.__get_param(1, comm)
                second = self.__get_param(2, comm)
                pos = self.commands[self.step + 3]
                if comm[3] == 2:
                    pos = pos + self.relative_base
                self.commands[pos] = 1 if first == second else 0

                self.step += 4

            elif comm[0] == 9:
                first = self.__get_param(1, comm)
                self.relative_base += first
                self.step += 2

            else:
                raise ValueError
