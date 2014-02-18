#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int next_collatz_number(int alpha)
{
  if(div(alpha,2).rem==0)
    {
      alpha=alpha/2;
    }
  else
    {
      alpha=3*alpha+1;
    }
  return alpha;
}

int sum;
int val,a;
float avg;
int main(int argv, char *argc[])
{
  
  for(a=1;a<1000;a++)
    {
      /* convert the loop run to the variable in question */
      val=a;
      while(val!=1)
	{
	  val=next_collatz_number(val);
	  sum=sum+1;
	}
      avg=pow(sum/a,3);
      printf("%d %f\n", a, avg);
    }
  return 0;
}
