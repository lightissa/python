from threading import Thread
class mythread(Thread):
      def run(self):
          print(,Bonjour du thread %s' %self.name)
for i in range(3):
  my_thread = mythread()
  my_thread.name=i
  my_thread.start()
