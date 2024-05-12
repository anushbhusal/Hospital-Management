
#include<stdio.h>
#include<string.h>
int main()
{
    char inp[100],k[50], temp[50], q[100],temp1[50], r[50], k1[50];
    int i, j , klen, inplen, rem=0;
    printf("Enter the message \n");
    scanf("%s", inp);
    printf("Enter the divisor \n");
    scanf("%s", k);
    klen = strlen(k);
    inplen = strlen(inp);
    strcpy(k1, k);
    for(i=0; i<klen-1; i++)
    {
        inp[inplen+i]='0';
    }
    for(i=0; i<klen; i++)
        temp[i]= inp[i];
    for(i=0; i<inplen; i++)
    {
        q[i]=temp[0];
        if(q[i]=='0')
        {

        for(j=0; j<klen; j++)
        {
            k[j]='0';
        }
        }
        else
        for(j=0; j<klen; j++)
        {
            k[j]=k1[j];
        }
        for(j=klen-1; j>0; j--)
        {
            if(temp[j]==k[j])
                r[j-1]='0';
            else
                r[j-1]='1';
        }
        r[klen-1]=inp[i+klen];
        strcpy(temp, r);
    }
    strcpy(r,temp);
    printf("\n The quotient is: ");
     for(i=0; i<inplen; i++)
    printf("%c", q[i]);
    printf("\n The remainder is: ");
    for(i=0; i<klen-1; i++)
        printf("%c", r[i]);

    printf("\n The final data to be sent is: ");
    for(i=0; i<inplen; i++)
        printf("%c", inp[i]);
    for(i=0; i<klen-1; i++)
        printf("%c",r[i]);
    printf("\n");
    printf("Enter the received data:");
    scanf("%s", temp1);
    for(i=0; i<klen; i++)
        temp[i]= temp1[i];
    for(i=0; i<inplen; i++)
    {
        if(q[i]=='0')
        for(j=0; j<klen; j++)
        {
            k[j]='0';
        }
        else
        for(j=0; j<klen; j++)
        {
            k[j]=k1[j];
        }
        for(j=klen-1; j>0; j--)
        {
            if(temp[j]==k[j])
                r[j-1]='0';
            else
                r[j-1]='1';
        }
        r[klen-1]=temp1[i+klen];
        strcpy(temp,r);
    }
    strcpy(r,temp);
    printf("\n The Quotient is: ");
    for(i=0; i<inplen; i++)
    printf("%c", q[i]);
    printf("\n Remainder is: ");
    for(i=0; i<klen-1; i++)
        printf("%c", r[i]);

    for(i=0; i<klen-1; i++)
    {
        if(r[i]=='1')
            rem=1;
        else
            rem=0;
    }
    if(rem==0)
        printf("\n No error");
    else
        printf("\n Error detected");


    return 0;


}
