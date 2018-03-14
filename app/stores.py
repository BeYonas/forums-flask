import itertools


class BaseStore(object):

    def __init__(self, data_provider, last_id):
        self._data_provider = data_provider
        self._last_id = last_id

    def get_all(self):
        return self._data_provider

    def add(self, item):
        item.id = self._last_id
        self._data_provider.append(item)
        self._last_id += 1

    def get_by_id(self, item_id):
        # search for item by id
        all_items = self.get_all()
        result = None
        for item in all_items:
            if item.id == item_id:
                result = item
                break
        return result

    def update(self, updated_item):
        # update item data
        all_items = self.get_all()
        for index, item in enumerate(all_items):
            if updated_item.id == item.id:
                all_items[index] = updated_item
                break

    def delete(self, item_id):
        # delete item by id
        all_items = self.get_all()
        item_to_delete = self.get_by_id(item_id)
        all_items.remove(item_to_delete)

    def entity_exists(self, item):
        # checks if an entity exists in a store
        result = True

        if self.get_by_id(item.id) is None:
            result = False

        return result


class MemberStore(BaseStore):
    members = []
    Last_id = 1

    def __init__(self):
        super(MemberStore, self).__init__(MemberStore.members, MemberStore.Last_id)

    def get_by_name(self, name):
        return (member for member in self.get_all() if member.name == name)

    def get_members_with_posts(self, posts_list):
        all_members = self.get_all()
        for member, post in itertools.product(all_members, posts_list):
            if post.member_id == member.id and post not in member.posts:
                member.posts.append(post)
        return (member for member in all_members)

    def get_top_ten(self, posts_list):
        sorted_members = sorted(self.get_members_with_posts(posts_list),
                                key=lambda member: len(member.posts),
                                reverse=True)
        return (member for member in sorted_members[:10])


class PostStore(BaseStore):
    posts = []
    Last_id = 1

    def __init__(self):
        super(PostStore, self).__init__(PostStore.posts, PostStore.Last_id)

    def get_posts_by_date(self):
        posts_list = self.get_all()
        posts_list.sort(key=lambda post: post.date)
        return (post for post in posts_list)
