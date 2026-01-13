class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m, n = len(matrix), len(matrix[0])
        m_left, m_right = 0, m

        # first loop runs until we find a row for our target
        while m_left < m_right:
            m_mid =  (m_left + m_right) // 2
            row = matrix[m_mid]
            # search whether the target could be in the row
            if row[0] <= target and row[n-1] >= target:
                n_left, n_right = 0, n
                # second loop to look in the selected row
                while n_left < n_right:
                    n_mid =  (n_left + n_right) // 2
                    # search whether n_mid is the target
                    if row[n_mid] == target:
                        return True
                    # search whether it's in the beginning of the row
                    elif row[n_mid] > target:
                        n_right = n_mid
                    # search whether it's at the end of the row
                    else:
                        n_left = n_mid + 1
                return False
            # search whether it's in an earlier row
            elif row[0] > target:
                m_right = m_mid
            # search whether it's in a later row
            else:
                m_left = m_mid + 1
        
        return False