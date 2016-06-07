#include <stdio.h>

/* 二分探索を行う関数 */
int binSearch(int a[], int length, int x) {
	int left = 0;		//探索対象に左端の要素番号
	int right = length - 1;		//右端の要素番号
	int mid;		//真ん中の要素番号
	int pos = -1;		//見つかった要素番号
	int n = 0;		//処理回数

	/* 探索を行う  */
	while (left <= right && pos == -1) {
		/* 処理カウント増加  */
		n++;

		/* 真ん中の要素番号を求める  */
		mid = (left + right)  / 2;

		/* 処理の途中経過を表示する  */
		printf("%d回目の処理:左端 = %d, 右端 = %d, 真ん中 = %d\n", n, left, right, mid);

		/* 真ん中の要素とみつける値を比較する  */
		if (a[mid] == x) {
			pos = mid;		//見つかった位置取得
		} else if (a[mid] > x) {
			right = mid - 1;		//前側に探索対象を絞る
		} else {
			left = mid + 1;		//後側に絞る
		}
	}

	return pos;
}


int main() {
	int a[10] = {13, 27, 33, 39, 48, 52, 61, 65, 74, 86 };
	int x = 61;
	printf("探索結果 = %d\n", binSearch(a, 10, x));
	return 0;


}
