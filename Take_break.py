import time
import webbrowser

total_breaks =3
break_count= 0
print("this program started on" +time.ctime())
while(break_count > total_breaks):
  time.sleep(10)
  webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
  break_count = break_count+1
