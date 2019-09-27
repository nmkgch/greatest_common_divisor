cnt=[]
kaisu=(int(input('対象の数値の数を入力してください：')))+1
for ji in range(1,kaisu):
    cnt.append(int(input(str(ji)+'個目の数値を入力してください：')))
cnt1=max(cnt)
cnt.remove(cnt1)
cnt2=max(cnt)
cnt.remove(cnt2)
while cnt1!=0 and cnt2!=0:
    cnt1=cnt1%cnt2
    cnt.append(cnt1)
    cnt.append(cnt2)
    cnt1=max(cnt)
    cnt.remove(cnt1)
    cnt2=max(cnt)
    cnt.remove(cnt2)
print(cnt1)