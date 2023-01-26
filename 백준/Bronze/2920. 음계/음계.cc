#include<stdio.h>;

int main(){
    int on, tw, th, fo, fi, si, se, ei;
    scanf("%d %d %d %d %d %d %d %d", &on, &tw, &th, &fo, &fi, &si, &se, &ei);
    if(on < tw && tw < th && th < fo && fo < fi && fi < si && si < se && se < ei) printf("ascending");
    else if(on > tw && tw > th && th > fo && fo > fi && fi > si && si > se && se > ei) printf("descending");
    else printf("mixed");
    return 0;
}