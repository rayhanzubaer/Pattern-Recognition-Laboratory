clc;
close all;

fprintf('CompleteLinkage\n');

n = 7;
m = n-1;
X = [
    4,4;
    8,4;
    15,8;
    20,6;
    21,10;
    24,4;
    24,12;
    ];


T_C = n;
c = zeros(n,n);

for j=1:n
    c(j,j) = 1;
end

% Calculating distance
dd = pdist(X);
D = squareform(dd);

for k = 1:m
    variable = 0;
    min = 100;
    p1 = 0;
    p2 = 0;
    
    for i=1:n
        for j=1:variable
            if(min > D(i,j))
                min = D(i,j);
                p1 = i;
                p2 = j;
            end
        end
        variable = variable + 1;
    end
    
    
    D(p1,p2) = 100;
    D(p2,p1) = 100;
    
    for i = 1:T_C
        % Ghachang corresponding row and col 
        if(c(p2,i) ~= 0)
            c(p1,i) = i;
            c(p2,i) = 0;
        end
        
        % Maximum distance in p1 col
        if(D(i,p1)<D(i, p2))
            D(i,p1) = D(i, p2);
            D(i, p2) = 100;
        else
            D(i, p2) = 100;
        end
        
        % Maximum distance in p1 row
        if(D(p1, i)<D(p2, i))
            D(p1, i) = D(p2, i);
            D(p2, i) = 100;
        else
            D(p2, i) = 100;
        end
        
    end
    
    for ci = 1:T_C
        % Exclude diagonal
        if(c(ci,ci) ~= 0)
            fprintf('{ ');
            for cj = 1:T_C
                % Exclude diagonal
                if(c(ci,cj) ~= 0)
                    fprintf('%i ',cj);
                end
            end
            fprintf('}\t');
        end
    end
    fprintf('\n');
end

