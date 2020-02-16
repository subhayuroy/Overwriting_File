#include<stdio.h>
#include<unistd.h>
#include<fcntl.h>
#include<stdlib.h>
#include<string.h>
#include<sys/stat.h>
int main(int arg, char *argv[])
{
	int fd, rc;
	char *buffer= "Testing a write: ";
	fd= open("./afile", O_RDWR | O_CREAT | O_TRUNC, S_IRUSR | S_IWUSR)
	rc= write(fd, buffer, strlen(buffer));
	printf("wrote %d bytes\n",rc);
	close(fd);
	exit(EXIT_SUCCESS);
}
