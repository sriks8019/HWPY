from __future__ import print_function, division
import cmd


class Calculator(cmd.Cmd):
      prompt = 'mycmd >>> '
      intro = 'cmd interpreter for deploy, kill, benchmark, report commands.'

      def do_deploy(self, line):
              #args = line.split()

              print('deploy')

      def help_deploy(self):
              print('\n'.join([
                      'deploy',
                      'Display text: deploy.'
              ]))

      def do_kill(self, line):
          # args = line.split()

          print('kill')

      def help_kill(self):
          print('\n'.join([
              'kill',
              'Display text: kill.'
          ]))

      def do_benchmark(self, line):
          # args = line.split()

          print('benchmark')

      def help_benchmark(self):
          print('\n'.join([
              'benchmark',
              'Display text: benchmark.'
          ]))

      def do_report(self, line):
          # args = line.split()

          print('report')

      def help_report(self):
          print('\n'.join([
              'report',
              'Display text: report.'
          ]))

      def do_EOF(self, line):
              print('bye, bye')
              return True


if __name__ == '__main__':
      Calculator().cmdloop()