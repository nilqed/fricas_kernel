<TeXmacs|1.99.2>

<style|<tuple|generic|varsession>>

<\body>
  <\session|fricas|default>
    <\output>
      \;

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ FriCAS Computer Algebra
      System\ 

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Version: FriCAS
      1.2.3

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Timestamp: Wed, May 07, 2014
      \ 3:39:04 PM

      \;

      \ \ \ 

      \;
    </output>

    <\unfolded-io>
      (3) -\<gtr\>\ 
    <|unfolded-io>
      <code|integrate(1/(x * (a+b*x)^(1/3)),x)>
    <|unfolded-io>
      \;

      <with|mode|math|<frac|-log(<sqrt|a|3>*<sqrt|b*x+a|3><rsup|2>+<sqrt|a|3><rsup|2>*<sqrt|b*x+a|3>+a)+2*log(<sqrt|a|3><rsup|2>*<sqrt|b*x+a|3>-a)+2*<sqrt|3>*atan(<frac|2*<sqrt|a|3><rsup|2>*<sqrt|b*x+a|3>+a|a*<sqrt|3>>)|2*<sqrt|a|3>>>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type:
      Union(Expression(Integer),...)
    </unfolded-io>

    <\unfolded-io>
      (4) -\<gtr\>\ 
    <|unfolded-io>
      <code|series(log(cot(x)),x = %pi/2)>
    <|unfolded-io>
      \;

      <with|mode|math|log(<frac|-2*x+\<pi\>|2>)+<frac|1|3>*(x-<frac|\<pi\>|2>)<rsup|2>+<frac|7|90>*(x-<frac|\<pi\>|2>)<rsup|4>+<frac|62|2835>*(x-<frac|\<pi\>|2>)<rsup|6>+<frac|127|18900>*(x-<frac|\<pi\>|2>)<rsup|8>+<frac|146|66825>*(x-<frac|\<pi\>|2>)<rsup|10>+O((x-<frac|\<pi\>|2>)<rsup|11>)>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type: GeneralUnivariatePowerSeries(Expression(Integer),x,%pi/2)
    </unfolded-io>

    <\unfolded-io>
      (5) -\<gtr\>\ 
    <|unfolded-io>
      <code|M:=matrix [ [x + %i,0], [1,-2] ]>
    <|unfolded-io>
      \;

      <with|mode|math|<matrix|<tformat|<table|<row|<cell|x+i>|<cell|0>>|<row|<cell|1>|<cell|-2>>>>>>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type:
      Matrix(Polynomial(Complex(Integer)))
    </unfolded-io>

    <\unfolded-io>
      (6) -\<gtr\>\ 
    <|unfolded-io>
      <code|inverse(M)>
    <|unfolded-io>
      \;

      <with|mode|math|<matrix|<tformat|<table|<row|<cell|<frac|1|x+i>>|<cell|0>>|<row|<cell|<frac|1|2*x+2*i>>|<cell|-<frac|1|2>>>>>>>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type: Union(Matrix(Fraction(Polynomial(Complex(Integer)))),...)
    </unfolded-io>

    <\unfolded-io>
      (7) -\<gtr\>\ 
    <|unfolded-io>
      <code|S := [3*x^3 + y + 1 = 0,y^2 = 4]>
    <|unfolded-io>
      \;

      <with|mode|math|[y+3*x<rsup|3>+1=0,y<rsup|2>=4]>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type:
      List(Equation(Polynomial(Integer)))
    </unfolded-io>

    <\unfolded-io>
      (8) -\<gtr\>\ 
    <|unfolded-io>
      <code|radicalSolve(S)>
    <|unfolded-io>
      \;

      <with|mode|math|[[y=2,x=-1],[y=2,x=<frac|-<sqrt|-3>+1|2>],[y=2,x=<frac|<sqrt|-3>+1|2>],[y=-2,x=<frac|1|<sqrt|3|3>>],[y=-2,x=<frac|<sqrt|-1>*<sqrt|3>-1|2*<sqrt|3|3>>],[y=-2,x=<frac|-<sqrt|-1>*<sqrt|3>-1|2*<sqrt|3|3>>]]>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type:
      List(List(Equation(Expression(Integer))))
    </unfolded-io>

    <\unfolded-io>
      (9) -\<gtr\>\ 
    <|unfolded-io>
      <code|continuedFraction(6543/210)>
    <|unfolded-io>
      \;

      <with|mode|math|31+<frac|1|6+<frac|1|2+<frac|1|1+<frac|1|3>>>>>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type:
      ContinuedFraction(Integer)
    </unfolded-io>

    <\unfolded-io>
      (11) -\<gtr\>\ 
    <|unfolded-io>
      <code|(3*a^4 + 27*a - 36)::Polynomial PrimeField 7>
    <|unfolded-io>
      \;

      <with|mode|math|3*a<rsup|4>+6*a+6>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type:
      Polynomial(PrimeField(7))
    </unfolded-io>

    <\unfolded-io>
      (12) -\<gtr\>\ 
    <|unfolded-io>
      <code|[i^2 for i in 1..10]>
    <|unfolded-io>
      \;

      <with|mode|math|[1,4,9,16,25,36,49,64,81,100]>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type:
      List(PositiveInteger)
    </unfolded-io>

    <\unfolded-io>
      (13) -\<gtr\>\ 
    <|unfolded-io>
      <code|[i for i in 1..10 \| even?(i)]>
    <|unfolded-io>
      \;

      <with|mode|math|[2,4,6,8,10]>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type:
      List(PositiveInteger)
    </unfolded-io>

    <\unfolded-io>
      (14) -\<gtr\>\ 
    <|unfolded-io>
      <code|[1..3,5,6,8..10]>
    <|unfolded-io>
      \;

      <with|mode|math|[1..3,5..5,6..6,8..10]>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type:
      List(Segment(PositiveInteger))
    </unfolded-io>

    <\unfolded-io>
      (15) -\<gtr\>\ 
    <|unfolded-io>
      <code|factor 643238070748569023720594412551704344145570763243>
    <|unfolded-io>
      \;

      <with|mode|math|11<rsup|13>*13<rsup|11>*17<rsup|7>*19<rsup|5>*23<rsup|3>*29<rsup|2>>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type:
      Factored(Integer)
    </unfolded-io>

    <\unfolded-io>
      (16) -\<gtr\>\ 
    <|unfolded-io>
      <code|roman(1992)>
    <|unfolded-io>
      \;

      <with|mode|math|MCMXCII>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type:
      RomanNumeral
    </unfolded-io>

    <\unfolded-io>
      (17) -\<gtr\>\ 
    <|unfolded-io>
      <code|(2/3 + %i)^3>
    <|unfolded-io>
      \;

      <with|mode|math|-<frac|46|27>+<frac|1|3>*i>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type:
      Complex(Fraction(Integer))
    </unfolded-io>

    <\unfolded-io>
      (18) -\<gtr\>\ 
    <|unfolded-io>
      <code|q:=quatern(1,2,3,4)*quatern(5,6,7,8) -
      quatern(5,6,7,8)*quatern(1,2,3,4)>
    <|unfolded-io>
      \;

      <with|mode|math|-8*i+16*j-8*k>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type:
      Quaternion(Integer)
    </unfolded-io>

    <\unfolded-io>
      (19) -\<gtr\>\ 
    <|unfolded-io>
      <code|matrix([ [1/(i + j - x) for i in 1..4] for j in 1..4])>
    <|unfolded-io>
      \;

      <with|mode|math|<matrix|<tformat|<table|<row|<cell|-<frac|1|x-2>>|<cell|-<frac|1|x-3>>|<cell|-<frac|1|x-4>>|<cell|-<frac|1|x-5>>>|<row|<cell|-<frac|1|x-3>>|<cell|-<frac|1|x-4>>|<cell|-<frac|1|x-5>>|<cell|-<frac|1|x-6>>>|<row|<cell|-<frac|1|x-4>>|<cell|-<frac|1|x-5>>|<cell|-<frac|1|x-6>>|<cell|-<frac|1|x-7>>>|<row|<cell|-<frac|1|x-5>>|<cell|-<frac|1|x-6>>|<cell|-<frac|1|x-7>>|<cell|-<frac|1|x-8>>>>>>>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type:
      Matrix(Fraction(Polynomial(Integer)))
    </unfolded-io>

    <\unfolded-io>
      (20) -\<gtr\>\ 
    <|unfolded-io>
      <code|p: UP(x,INT) := (3*x-1)^2 * (2*x + 8)>
    <|unfolded-io>
      \;

      <with|mode|math|18*x<rsup|3>+60*x<rsup|2>-46*x+8>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type:
      UnivariatePolynomial(x,Integer)
    </unfolded-io>

    <\unfolded-io>
      (21) -\<gtr\>\ 
    <|unfolded-io>
      <code|g := csc(a*x) / csch(b*x)>
    <|unfolded-io>
      \;

      <with|mode|math|<frac|csc(a*x)|csch(b*x)>>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type:
      Expression(Integer)
    </unfolded-io>

    <\unfolded-io>
      (22) -\<gtr\>\ 
    <|unfolded-io>
      <code|limit(g,x=0)>
    <|unfolded-io>
      \;

      <with|mode|math|<frac|b|a>>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type:
      Union(OrderedCompletion(Expression(Integer)),...)
    </unfolded-io>

    <\unfolded-io>
      (23) -\<gtr\>\ 
    <|unfolded-io>
      <code|h := (1 + k/x)^x>
    <|unfolded-io>
      \;

      <with|mode|math|<frac|x+k|x><rsup|x>>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type:
      Expression(Integer)
    </unfolded-io>

    <\unfolded-io>
      (24) -\<gtr\>\ 
    <|unfolded-io>
      <code|limit(h,x=%plusInfinity)>
    <|unfolded-io>
      \;

      <with|mode|math|e<rsup|k>>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type:
      Union(OrderedCompletion(Expression(Integer)),...)
    </unfolded-io>

    <\unfolded-io>
      (25) -\<gtr\>\ 
    <|unfolded-io>
      <code|series(sin(a*x),x = 0)>
    <|unfolded-io>
      \;

      <with|mode|math|a*x-<frac|a<rsup|3>|6>*x<rsup|3>+<frac|a<rsup|5>|120>*x<rsup|5>-<frac|a<rsup|7>|5040>*x<rsup|7>+<frac|a<rsup|9>|362880>*x<rsup|9>-<frac|a<rsup|11>|39916800>*x<rsup|11>+O(x<rsup|12>)>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type:
      UnivariatePuiseuxSeries(Expression(Integer),x,0)
    </unfolded-io>

    <\unfolded-io>
      (26) -\<gtr\>\ 
    <|unfolded-io>
      <code|series(sin(a*x),x = %pi/4)>
    <|unfolded-io>
      \;

      <with|mode|math|sin(<frac|a*\<pi\>|4>)+a*cos(<frac|a*\<pi\>|4>)*(x-<frac|\<pi\>|4>)-<frac|a<rsup|2>*sin(<frac|a*\<pi\>|4>)|2>*(x-<frac|\<pi\>|4>)<rsup|2>-<frac|a<rsup|3>*cos(<frac|a*\<pi\>|4>)|6>*(x-<frac|\<pi\>|4>)<rsup|3>+<frac|a<rsup|4>*sin(<frac|a*\<pi\>|4>)|24>*(x-<frac|\<pi\>|4>)<rsup|4>+<frac|a<rsup|5>*cos(<frac|a*\<pi\>|4>)|120>*(x-<frac|\<pi\>|4>)<rsup|5>-<frac|a<rsup|6>*sin(<frac|a*\<pi\>|4>)|720>*(x-<frac|\<pi\>|4>)<rsup|6>-<frac|a<rsup|7>*cos(<frac|a*\<pi\>|4>)|5040>*(x-<frac|\<pi\>|4>)<rsup|7>+<frac|a<rsup|8>*sin(<frac|a*\<pi\>|4>)|40320>*(x-<frac|\<pi\>|4>)<rsup|8>+<frac|a<rsup|9>*cos(<frac|a*\<pi\>|4>)|362880>*(x-<frac|\<pi\>|4>)<rsup|9>-<frac|a<rsup|10>*sin(<frac|a*\<pi\>|4>)|3628800>*(x-<frac|\<pi\>|4>)<rsup|10>+O((x-<frac|\<pi\>|4>)<rsup|11>)>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type:
      UnivariatePuiseuxSeries(Expression(Integer),x,%pi/4)
    </unfolded-io>

    <\unfolded-io>
      (27) -\<gtr\>\ 
    <|unfolded-io>
      <code|series(n +-\<gtr\> (-1)^((3*n - 4)/6)/factorial(n -
      1/3),x=0,4/3..,2)>
    <|unfolded-io>
      \;

      <with|mode|math|x<rsup|<frac|4|3>>-<frac|1|6>*x<rsup|<frac|10|3>>+O(x<rsup|5>)>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type:
      UnivariatePuiseuxSeries(Expression(Integer),x,0)
    </unfolded-io>

    <\unfolded-io>
      (28) -\<gtr\>\ 
    <|unfolded-io>
      <code|f := taylor(exp(x))>
    <|unfolded-io>
      \;

      <with|mode|math|1+x+<frac|1|2>*x<rsup|2>+<frac|1|6>*x<rsup|3>+<frac|1|24>*x<rsup|4>+<frac|1|120>*x<rsup|5>+<frac|1|720>*x<rsup|6>+<frac|1|5040>*x<rsup|7>+<frac|1|40320>*x<rsup|8>+<frac|1|362880>*x<rsup|9>+<frac|1|3628800>*x<rsup|10>+O(x<rsup|11>)>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type:
      UnivariateTaylorSeries(Expression(Integer),x,0)
    </unfolded-io>

    <\unfolded-io>
      (29) -\<gtr\>\ 
    <|unfolded-io>
      <code|F := operator 'F; x := operator 'x; y := operator 'y>
    <|unfolded-io>
      \;

      <with|mode|math|y>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type:
      BasicOperator
    </unfolded-io>

    <\unfolded-io>
      (30) -\<gtr\>\ 
    <|unfolded-io>
      <code|a := F(x z, y z, z^2) + x y(z+1)>
    <|unfolded-io>
      \;

      <with|mode|math|x(y(z+1))+F(x(z),y(z),z<rsup|2>)>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type:
      Expression(Integer)
    </unfolded-io>

    <\unfolded-io>
      (31) -\<gtr\>\ 
    <|unfolded-io>
      <code|dadz := D(a, z)>
    <|unfolded-io>
      \;

      <with|mode|math|2*z*F<rsub|,3>(x(z),y(z),z<rsup|2>)+y<rsup|,>(z)*F<rsub|,2>(x(z),y(z),z<rsup|2>)+x<rsup|,>(z)*F<rsub|,1>(x(z),y(z),z<rsup|2>)+x<rsup|,>(y(z+1))*y<rsup|,>(z+1)>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type:
      Expression(Integer)
    </unfolded-io>

    <\unfolded-io>
      (32) -\<gtr\>\ 
    <|unfolded-io>
      <code|eval(eval(dadz, 'x, z +-\<gtr\> exp z), 'y, z +-\<gtr\>
      log(z+1))>
    <|unfolded-io>
      \;

      <with|mode|math|<frac|(2*z<rsup|2>+2*z)*F<rsub|,3>(e<rsup|z>,log(z+1),z<rsup|2>)+F<rsub|,2>(e<rsup|z>,log(z+1),z<rsup|2>)+(z+1)*e<rsup|z>*F<rsub|,1>(e<rsup|z>,log(z+1),z<rsup|2>)+z+1|z+1>>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type:
      Expression(Integer)
    </unfolded-io>

    <\unfolded-io>
      (33) -\<gtr\>\ 
    <|unfolded-io>
      <code|eval(eval(a, 'x, z +-\<gtr\> exp z), 'y, z +-\<gtr\> log(z+1))>
    <|unfolded-io>
      \;

      <with|mode|math|F(e<rsup|z>,log(z+1),z<rsup|2>)+z+2>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type:
      Expression(Integer)
    </unfolded-io>

    <\unfolded-io>
      (34) -\<gtr\>\ 
    <|unfolded-io>
      <code|D(%, z)>
    <|unfolded-io>
      \;

      <with|mode|math|<frac|(2*z<rsup|2>+2*z)*F<rsub|,3>(e<rsup|z>,log(z+1),z<rsup|2>)+F<rsub|,2>(e<rsup|z>,log(z+1),z<rsup|2>)+(z+1)*e<rsup|z>*F<rsub|,1>(e<rsup|z>,log(z+1),z<rsup|2>)+z+1|z+1>>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type:
      Expression(Integer)
    </unfolded-io>

    <\unfolded-io>
      (35) -\<gtr\>\ 
    <|unfolded-io>
      <code|integrate(1/(u^2 + a),u)>
    <|unfolded-io>
      \;

      <with|mode|math|[<frac|log(<frac|(-x(y(z+1))-F(x(z),y(z),z<rsup|2>)+u<rsup|2>)*<sqrt|-x(y(z+1))-F(x(z),y(z),z<rsup|2>)>+2*u*x(y(z+1))+2*u*F(x(z),y(z),z<rsup|2>)|x(y(z+1))+F(x(z),y(z),z<rsup|2>)+u<rsup|2>>)|2*<sqrt|-x(y(z+1))-F(x(z),y(z),z<rsup|2>)>>,<frac|atan(<frac|u*<sqrt|x(y(z+1))+F(x(z),y(z),z<rsup|2>)>|x(y(z+1))+F(x(z),y(z),z<rsup|2>)>)|<sqrt|x(y(z+1))+F(x(z),y(z),z<rsup|2>)>>]>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type:
      Union(List(Expression(Integer)),...)
    </unfolded-io>

    <\unfolded-io>
      (36) -\<gtr\>\ 
    <|unfolded-io>
      <code|integrate(log(1 + sqrt(a*u + b)) / u,u)>
    <|unfolded-io>
      \;

      <with|mode|math|<big-around|\<int\>|<rsub|><rsup|u><frac|log(<sqrt|%A*x(y(z+1))+%A*F(x(z),y(z),z<rsup|2>)+b>+1)|%A>*\<mathd\>%A<big|.>>>

      \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Type:
      Union(Expression(Integer),...)
    </unfolded-io>

    <\unfolded-io>
      (37) -\<gtr\>\ 
    <|unfolded-io>
      )quit
    <|unfolded-io>
      \;

      <script-busy>
    </unfolded-io>

    <\input>
      (37) -\<gtr\>\ 
    <|input>
      \;
    </input>
  </session>
</body>

<initial|<\collection>
</collection>>