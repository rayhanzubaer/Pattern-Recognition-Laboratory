function E = getE(x1,x2,x3,d)
    if(nargin==2)
        d = x2;
        syms('w0');
        syms('w1');
        E = (w0+w1*x1-d)^2;
        
    elseif(nargin==3)
        d = x3;
        syms('w0');
        syms('w1');
        syms('w2');
        E = (w0+w1*x1+w2*x2-d)^2;
    elseif(nargin==4)
        syms('w0');
        syms('w1');
        syms('w2');
        syms('w3');
        E = (w0+w1*x1+w2*x2+w3*x3-d)^2;
    end
end