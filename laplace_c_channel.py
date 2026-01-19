import numpy as np
import matplotlib.pyplot as plt

def gauss_seidel_c_channel(M, N, c, mu, max_iter, tol):
    """
    Giai phuong trinh Poisson trong kenh chu C
    """
    # Buoc luoi
    dx = 6.0 / (M + 1)
    dy = 6.0 / (N + 1)

    # Khoi tao
    phi = np.zeros((N + 2, M + 2))

    # Ap dung dieu kien bien: phi = 0 tai tat ca cac thanh
    # (Mac dinh da la 0)

    # He so phai
    # (Dựa trên công thức 23 trang 10 và dòng 225 trong nguồn OCR)
    rhs = c * dx * dx / mu 

    # Vong lap Gauss-Seidel
    for n in range(max_iter):
        phi_old = phi.copy()

        # Cap nhat cac diem ben trong
        for j in range(1, N + 1):
            for i in range(1, M + 1):
                # Kiem tra xem diem (i,j) co nam trong mien tinh toan
                if is_inside_domain(i, j, M, N):
                    phi[j, i] = 0.25 * (phi[j, i+1] + phi[j, i-1] + 
                                        phi[j+1, i] + phi[j-1, i] - rhs)

        # Kiem tra hoi tu
        error = np.sum(np.abs(phi - phi_old))
        if error < tol:
            print(f"Hoi tu tai buoc lap thu {n}")
            return phi

    print("Chua hoi tu sau", max_iter, "buoc lap")
    return phi

def is_inside_domain(i, j, M, N):
    """
    Kiem tra xem diem (i,j) co nam trong mien tinh toan hinh chu C
    """
    # Logic de xac dinh hinh chu C
    # Can dieu chinh dua tren hinh hoc cu the
    return True