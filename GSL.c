#include <stdio.h>
#include <gsl/gsl_linalg.h>
int m=3;
int main()
{
    double S[] = {1, 0.67, 0.33, 0.45, 1, 0.55, 0.67, 0.33, 1};//the given matrix
    int i,k,j;
    int key = 0;

    gsl_matrix *M = gsl_matrix_alloc(m, m);
    gsl_matrix *A = gsl_matrix_alloc(m, m);

    printf("A = \n");
    for(i = 0;i<m;i=i+1)
    {
      for(k=0;k<m;k=k+1)
      {
        gsl_matrix_set(M,i,k,S[i*m+k]);
        gsl_matrix_set(A,i,k,S[i*m+k]);
        printf("%0.2f\t\t",S[i*m+k]);
      }
      printf("\n");
    }
    printf("\n");

    int sign;
    gsl_permutation *p = gsl_permutation_alloc(m);


    gsl_linalg_LU_decomp(M, p, &sign);

    gsl_matrix *U = gsl_matrix_alloc(m,m);
    gsl_matrix *L = gsl_matrix_alloc(m,m);

    printf("U = \n");

    for (i=0;i<m;i=i+1)
    {
      for (k = 0;k<m;k=k+1)
      {
        if(k<i)
          {printf("0.00\t\t");gsl_matrix_set(U,i,k,0);}
        else
        {printf("%0.2f\t\t",gsl_matrix_get(M,i,k));gsl_matrix_set(U,i,k,gsl_matrix_get(M,i,k));}
      }
      printf("\n");
    }
    printf("\n");


    printf("L = \n");

    for(i=0;i<m;i=i+1)
    {
      for(k=0;k<m;k=k+1)
      {
        if(k>i)
          {printf("0.00\t\t");gsl_matrix_set(L,i,k,0);}
        else
        {
          if(k == i)
            {printf("1.00\t\t");gsl_matrix_set(L,i,k,1);}
          else
            {printf("%0.2f\t\t",gsl_matrix_get(M,i,k));gsl_matrix_set(L,i,k,gsl_matrix_get(M,i,k));}
        }
      }
      printf("\n");
    }
    printf("\n");


    gsl_matrix *P = gsl_matrix_alloc(m,m);
    gsl_matrix *Identity = gsl_matrix_alloc(m,m);
    gsl_matrix_set_identity(Identity);

    printf("P = \n");

    for(i=0;i<m;i=i+1)
    {
      for(k=0;k<m;k=k+1)
      {
        gsl_matrix_set(P,i,k,gsl_matrix_get(Identity,i,gsl_permutation_get(p,k)));
        printf("%0.2f\t\t",gsl_matrix_get(P,i,k));
      }
      printf("\n");
    }


    double s = 0;
    double s1 = 0;

    for(i = 0;i<m;i=i+1)
    {
      for(k=0;k<m;k=k+1)
      {
        for(j=0;j<m;j=j+1)
        {
          s = s + gsl_matrix_get(P,i,j)*gsl_matrix_get(A,j,k);
          s1 = s1 + gsl_matrix_get(L,i,j)*gsl_matrix_get(U,j,k);
        }
        if(s != s1)
          key = 1;
        s = 0;
        s1 = 0;
      }
    }

    if(key == 1)
      printf("PA is not equal to LU\n");
    else
      printf("PA is equal to LU\n");


    gsl_permutation_free(p);
    gsl_matrix_free(M);
    gsl_matrix_free(U);
    gsl_matrix_free(L);
    gsl_matrix_free(P);
    gsl_matrix_free(Identity);
    return 0;
}
