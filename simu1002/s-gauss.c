#include<stdio.h>
#define TIMES 20

//ax+by+cz=d
float third_calc(float d,float variable1,float variable2,float coefficient);

int main(void)
{
  int i;
  float x = 1;
  float y = 1;
  float z = 1;

  for(i=0;i<TIMES;i++){
    printf("%2d:  x:%6f y:%6f z:%6f\n",i,x,y,z);
    x = third_calc(10,y,z,5);
    y = third_calc(12,x,z,4);
    z = third_calc(13,y,2*x,3);
  }

  return 0;
}

float third_calc(float d,float variable1,float variable2,float coefficient)
{
  return (d-variable1-variable2)/coefficient;
}
