from typing import List
import collections
import heapq


class FileSharing:

    def __init__(self, m: int):
        self.counter = 1
        self.min_heap = []
        self.chunk_to_owner = collections.defaultdict(set)
        self.owner_to_chunk = collections.defaultdict(set)

    def join(self, ownedChunks: List[int]) -> int:
        # Reuser ID
        if self.min_heap:
            user_id = heapq.heappop(self.min_heap)
        else:
            user_id = self.counter
            self.counter += 1

        self.owner_to_chunk[user_id] = set(ownedChunks)

        for chunk_id in ownedChunks:
            self.chunk_to_owner[chunk_id].add(user_id)

        return user_id

    def leave(self, userID: int) -> None:
        heapq.heappush(self.min_heap, userID)
        chunk_ids = self.owner_to_chunk.pop(userID)
        for chunk_id in chunk_ids:
            self.chunk_to_owner[chunk_id].remove(userID)

    def request(self, userID: int, chunkID: int) -> List[int]:
        ans = sorted(self.chunk_to_owner[chunkID])
        if ans:
            self.chunk_to_owner[chunkID].add(userID)
            self.owner_to_chunk[userID].add(chunkID)
        return ans


# Your FileSharing object will be instantiated and called as such:
# obj = FileSharing(m)
# param_1 = obj.join(ownedChunks)
# obj.leave(userID)
# param_3 = obj.request(userID,chunkID)