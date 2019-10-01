clc;
close all;
fprintf('CompleteLinkage');
fprintf('\n');
totalSamples = 7;
mainLoop = totalSamples-1;
samples  = [
    4,4;
    8,4;
    15,8;
    20,6;
    21,10;
    24,4;
    24,12;
    ];
totalCluster = totalSamples;
cluster = zeros(totalSamples,totalSamples);

for j=1:totalSamples
    cluster(j,j) = 1;
end

for i=1:totalSamples
    for j=1:totalSamples
        if(i==j)
            distance(i,j) = 9999;
        else
            distance(i, j) = sqrtm((samples(i,1)-samples(j,1))*(samples(i,1)-samples(j,1))+(samples(i,2)-samples(j,2))*(samples(i,2)-samples(j,2)));
        end
        
    end
end

for k = 1:mainLoop
    variable = 0;
    checkDist = 9990;
    smallI = 0;
    smallJ = 0;
    
    for i=1:totalSamples
        for j=1:variable
            if(checkDist > distance(i,j))
                checkDist = distance(i,j);
                smallI = i;
                smallJ = j;
            end
        end
        variable = variable + 1;
    end
    
    %     checkDist
    %     smallI
    %     smallJ
    distance(smallI,smallJ) = 9999;
    distance(smallJ,smallI) = 9999;
    
    for i = 1:totalCluster
        if(cluster(smallJ,i) ~= 0)
            cluster(smallI,i) = i;
            cluster(smallJ,i) = 0;
        end
        if(distance(i, smallI)<distance(i, smallJ))
            distance(i, smallI) = distance(i, smallJ);
            distance(i, smallJ) = 9999;
        else
            distance(i, smallJ) = 9999;
        end
        if(distance(smallI, i)<distance(smallJ, i))
            distance(smallI, i) = distance(smallJ, i);
            distance(smallJ, i) = 9999;
        else
            distance(smallJ, i) = 9999;
        end
        
    end
    
    for ci = 1:totalCluster
        if(cluster(ci,ci) ~= 0)
            fprintf('{');
            for cj = 1:totalCluster
                if(cluster(ci,cj) ~= 0)
                    fprintf(' %i ',cj);
                end
            end
            fprintf('}\t');
        end
    end
    fprintf('\n');
    
    %     distance
end

