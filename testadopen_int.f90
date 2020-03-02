integer, allocatable :: d(:,:)
integer :: nrows, ncols
integer :: readvalues(2)

nrows = 2
ncols = 3

allocate(d(nrows,ncols))

open(10,file='test.ad',access='direct',form='unformatted',recl=4*2)

! colunas
do i=1,ncols
  ! linhas
  do j=1,nrows
    read(10,rec=2*(i-1)+j) readvalues
    !write(*,*) readvalues(2)
    d(j,i) = readvalues(2)
  enddo
enddo


! testing

! linhas
do j=1,nrows
  ! colunas
  write(*,*) d(j,:)
enddo


deallocate(d)
stop
end
