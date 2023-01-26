#include <stdio.h>
# define SWAP(x, y, temp) ( (temp)=(x), (x)=(y), (y)=(temp) )

int partition(int list[], int left, int right){
  int pivot, temp;
  int low, high;

  low = left;
  high = right + 1;
  pivot = list[left]; // 정렬할 리스트의 가장 왼쪽 데이터를 피벗으로 선택(임의의 값을 피벗으로 선택)

  /* low와 high가 교차할 때까지 반복(low<high) */
  do{
    /* list[low]가 피벗보다 작으면 계속 low를 증가 */
    do {
      low++; // low는 left+1 에서 시작
    } while (low<=right && list[low]<pivot);

    /* list[high]가 피벗보다 크면 계속 high를 감소 */
    do {
      high--; //high는 right 에서 시작
    } while (high>=left && list[high]>pivot);

    // 만약 low와 high가 교차하지 않았으면 list[low]를 list[high] 교환
    if(low<high){
      SWAP(list[low], list[high], temp);
    }
  } while (low<high);

  // low와 high가 교차했으면 반복문을 빠져나와 list[left]와 list[high]를 교환
  SWAP(list[left], list[high], temp);

  // 피벗의 위치인 high를 반환
  return high;
}

// 퀵 정렬
void quick_sort(int list[], int left, int right){

  /* 정렬할 범위가 2개 이상의 데이터이면(리스트의 크기가 0이나 1이 아니면) */
  if(left<right){
    // partition 함수를 호출하여 피벗을 기준으로 리스트를 비균등 분할 -분할(Divide)
    int q = partition(list, left, right); // q: 피벗의 위치

    // 피벗은 제외한 2개의 부분 리스트를 대상으로 순환 호출
    quick_sort(list, left, q-1); // (left ~ 피벗 바로 앞) 앞쪽 부분 리스트 정렬 -정복(Conquer)
    quick_sort(list, q+1, right); // (피벗 바로 뒤 ~ right) 뒤쪽 부분 리스트 정렬 -정복(Conquer)
  }

}

int main(){
  int num[9];
  int newnum[7];
  int sum=0;
  int x=0;
  int no1=0,no2=0;
  for(int i=0;i<9;i++){
    scanf("%d",&num[i]);
    sum+=num[i];
  }

  for(int i=0;i<81;i++){
      if((sum-num[i%9]-num[i/9])==100 && i%9!=i/9){
        no1=i%9;
        no2=i/9;
      }        
  }
  //printf("%d %d\n",no1,no2);

  for(int i=0;i<9;i++){
    if(i!=no1 && i!=no2){
      newnum[x]=num[i];
      x++;
    }  
  }
/*
  for(int i=0;i<7;i++){
    printf("\n%d",newnum[i]);
  }
*/
  printf("\n");

  quick_sort(newnum,0,6);

  for(int i=0;i<7;i++){
    printf("\n%d",newnum[i]);
  }

}