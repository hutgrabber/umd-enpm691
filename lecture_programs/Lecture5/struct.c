#include <stdio.h>


//L5 slides 35-38 (est)
struct rec {
  int a[3];
  int i;
  struct rec *n;
};

void set_i(struct rec *r, int val)
{
  r->i = val;
}

int *get_ap(struct rec *r, int idx)
{
  return &r->a[idx];
}

void set_val(struct rec *r, int val)
{
  while (r) {
    int i = r->i;
    r->a[i] = val;
    r = r->n;
  }
}

//L5 slide 39,43-44
struct S1 {
  char c;
  int i[2];
  double v;
};

//L5 slide 45-46
struct S2 {
  double v;
  int i[2];
  char c;
};

//L5 slide 47
struct S3 {
  short i;
  float v;
  short j;
};

//L5 slide 48
struct S4 {
  char c;
  int i;
  char d;
}; 

//L5 slide 48
struct S5 {
  int i;
  char c;
  char d;
};

int main()
{
    struct rec r1 = { {1,2,3} , 4, &r1 };   
    struct S1  s1 = { 'A', {5,6}, 3.1415926 };
    struct S2  s2 = { 2.71828, {7,8}, 'B' };
    struct S3  s3 = { 1024, 1.41421, 2048 };
    struct S4  s4 = { 'D', 42, 'E' };
    struct S5  s5 = { 42, 'D', 'E' };


    set_i( &r1, 44);

    get_ap( &r1, 1);

    set_val ( &r1, 99);

    return 0;
}
