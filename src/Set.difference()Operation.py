e_news = int(input())
e_news_stu_rno = set(map(int, input().split()))
f_news = int(input())
f_news_stu_rno = set(map(int, input().split()))
total_e_news_stu = e_news_stu_rno.difference(f_news_stu_rno)
print(len(total_e_news_stu))