% SquaredError
function [anss]= SquaredError(input,sample)
     sample = [4 4;
               8 4;
               15 8;
               24 4;
               24 12;];

    input = [1 2 5];
    if(length(input) == 1)
        anss = 0;
    else
        a = 0;
        b = 0;
        anss = 0;
        for i = 1:length(input)
            a = a+sample(input(i),1);
            b = b+sample(input(i),2);
        end
        a = a/length(input);
        b = b/length(input);
        for i = 1:length(input)
            anss = anss + power((sample(input(i),1)-a),2);
            anss = anss + power((sample(input(i),2)-b),2);
        end
%         anss
    end
end
