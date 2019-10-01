function [Y]= findd(P,k,x1,y1)
dis=zeros(k,2);
for i=1:k
    dis(i,1)=i;
    dis(i,2)=sqrt(power((x1-P(i,2)),2)+power((y1-P(i,3)),2));
end
sortDis=sortrows(dis,2);
Y=sortDis(1,1);
end
