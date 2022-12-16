#include <iostream>
#include <vector>
#include <random>
#include <chrono>
#include <Eigen/Dense>

int main() {
    constexpr auto N = 1000;

    std::mt19937 mt(12345);
    std::normal_distribution<double> dist(0.0, 1.0);
    std::vector<double> mat(N*N, 0.0);
    for (int i=0; i<N; i++) {
        for (int j=i; j<N; j++) {
            mat[N*i + j] = dist(mt);
            mat[N*j + i] = mat[N*i + j];
        }
    }

    Eigen::Map<Eigen::MatrixXd> p(mat.data(), N, N);
    auto start = std::chrono::system_clock::now();
    Eigen::SelfAdjointEigenSolver<Eigen::MatrixXd> es(p);
    auto end = std::chrono::system_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::microseconds>(end-start).count();

    std::cout << elapsed*1e-3 << std::endl;
}
