subroutine calcpos(nrows,ncols,i,j,k)
  implicit none
  integer, intent(in)  :: nrows, ncols, i
  integer, intent(out) :: j, k
  j=1+(i-1)/ncols
  k=1+mod(i-1,ncols)
end subroutine calcpos


program nc2ad
  real(4), allocatable :: d(:,:)
  real(4)              :: pastvalues(2), newvalues(2)
  integer              :: nrows, ncols
  integer              :: h, i, j, k



  open(10,file='test_array_z_4_4.ad',access='direct',form='unformatted',recl=8)
  nrows = 4
  ncols = 3
  n     = nrows*ncols
  allocate(d(nrows,ncols))

  ! abrindo dado
  ! colunas

  read(10,rec=1) pastvalues
  do h=2,n/2+1
    read(10,rec=h) newvalues

    i=1+2*(h-2)
    call calcpos(nrows,ncols,i,j,k)
    !write(*,*) i,j,k, pastvalues(2)
    d(j,k) = pastvalues(2)

    i=i+1
    call calcpos(nrows,ncols,i,j,k)
    !write(*,*) i,j,k, newvalues(1)
    d(j,k) = newvalues(1)

    pastvalues(1:2) = newvalues(1:2)
  enddo



  ! testing

  ! linhas
  do j=1,nrows
    ! colunas
    write(*,*) d(j,:)
  enddo


  deallocate(d)
  stop
end program
