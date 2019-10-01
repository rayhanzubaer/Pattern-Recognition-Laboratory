function [X,Y,flag]=avrg(X,rM,i)
sumx=0;
sumy=0;
count=0;
for j=1:length(X)
  if(rM(j,2)==i)
      sumx=sumx+X(j,2);
      sumy=sumy+X(j,3);
      count=count+1;
  end
end
X=sumx/count;
Y=sumy/count;
flag=1;
if(count==0)
    flag=0;
end
end