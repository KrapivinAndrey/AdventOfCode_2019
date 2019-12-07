class IntComputer:

    def __init__(self, init_commands, init_val):
        self.commands = init_commands.copy()
        self.init_val = init_val
        self.step = 0

        self.in_val = 0
        self.out_val = 0
        self.state = 0

    def __prepare_comm(self):
        comm = self.commands[self.step]
        temp = "{:05d}".format(comm)
        res = [int(temp[-2:]),
               1 if temp[2] == '1' else 0,
               1 if temp[1] == '1' else 0,
               1 if temp[0] == '1' else 0]
        return res

    def __get_param(self, move, comm):
        param = self.commands[self.step + move]
        return self.commands[param] if comm[move] == 0 else param

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
                self.commands[pos] = first + second

                self.step += 4

            elif comm[0] == 2:
                first = self.__get_param(1, comm)
                second = self.__get_param(2, comm)
                pos = self.commands[self.step + 3]
                self.commands[pos] = first * second

                self.step += 4

            elif comm[0] == 3:
                pos = self.commands[self.step + 1]
                self.commands[pos] = self.init_val if self.state == 0 else self.in_val
                self.state = 1

                self.step += 2

            elif comm[0] == 4:
                pos = self.__get_param(1, comm)
                self.out_val = pos
                self.step += 2
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
                self.commands[pos] = 1 if first < second else 0

                self.step += 4

            elif comm[0] == 8:
                first = self.__get_param(1, comm)
                second = self.__get_param(2, comm)
                pos = self.commands[self.step + 3]
                self.commands[pos] = 1 if first == second else 0

                self.step += 4

            else:
                raise ValueError
