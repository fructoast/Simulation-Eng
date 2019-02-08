/*
 * IEEE754(単精度)の浮動小数点表現を実際に見てみる
 */

#include <stdio.h>

#define BIT 32

float binary2deci(int bit[]);

int main(void)
{
  int i, j, bit[BIT];
  float x;

  printf("num = ");
  scanf("%f", &x);
  printf("\n");

/* float型とint型は同じ32ビットなので，int型にキャスト．
 * 同じビット列でint型になる．これをビットシフトして中身を確認する．
 */
  j = *(int *)&x; 
  printf("j=%d\n", j);
  
  /* ビット列を1つずつ確認 */
  for (i=0; i<BIT; i++) {
    bit[i] = (j>>i) & 1;
  }

  /* 4bit区切りで表示 */
  printf("%f -> ", x);
  for (i=BIT-1; i>=0; i--) {
    printf("%d", bit[i]);
    if(i%4==0) {
      printf(" ");
    }
  }
  printf("\n\n");

  /* IEEE754がわかりやすくなるように区切って表示 */
  printf("%f -> ", x);
  for (i=BIT-1; i>=0; i--) {
    printf("%d", bit[i]);
    if(i==BIT-1 || i==BIT-8-1) {
      printf(" ");
    }
  }
  printf("\n\n");

  printf("復元\n%f\n",binary2deci(bit));
  

  return 0;
}

float binary2deci(int bit[])
{
  int i,j,degree;
  //int sign;         //符号
  int sumeddegree;  //次数の計
  float result;    //結果

  //sign = bit[31];    //符号はそのまま
  sumeddegree = 0;

  //次数を求めてビットと掛ける
  for(i=0;i<8;i++){ 
    degree= 1;
    
    for(j=0;j<i;j++){
      degree *= 2;
    }
    
    sumeddegree += degree * bit[31-(8-i)];
  }

  if(bit[31] == 1){
    result = -1;
  }
  else{
    result = 1;
  }

  //中身
  for(i=0;i<23;i++){
    degree = 2;
    
    for(j=0;j<i;j++){
      degree *= 2;
    }

    //bit[31-(9+i)]とdegree自体は生きてる
    //resultに入らない,桁落ち?
    result = result + (float)((bit[31-(9+i)])/degree);
    printf("result:%f\n",(float)(bit[31-(9+i)]/degree));
  }
  //  printf("1/8192:%f\n",(float)1/8192);

  /*
  for(i=0;i<sumeddegree;i++){
    result *= 2;
  }
  */
  
  return result;
}
