__all__ = ['fetch_PRs', 'update_papers']

import urllib3

import json
import os
from os.path import join as joinp


from builder import cache
pr_list_file = joinp(cache(), 'pr_info.json')


def fetch_PRs(user, repo, state='open'):
    fields = {'state': state,
              'per_page': 100,
              'page': 1}

    config = {'user': user,
              'repo': repo}
    config = dict(config.items() + fields.items())


    data = []
    page_data = True

    url = 'https://api.github.com/repos/%(user)s/%(repo)s/pulls' % config
    http = urllib3.PoolManager()

    while page_data:
        fetch_status = 'Fetching page %(page)d (state=%(state)s)' % fields + \
                       ' from %(user)s/%(repo)s...' % config
        print fetch_status

        response = http.request('GET', url, fields=fields,
                                headers={'user-agent': 'scipy-procbuild/0.1'})

        fields['page'] += 1

        page_data = json.loads(response.data)

        if 'message' in page_data and page_data['message'] == "Not Found":
            page_data = []
            print 'Warning: Repo not found (%(user)s/%(repo)s)' % config
        else:
            data.extend(page_data)

    return data


def update_papers():
    PRs = fetch_PRs(user='scipy-conference', repo='scipy_proceedings', state='open')

    PRs = [p for p in PRs if p['title'].startswith('Paper:')]

    pr_info = []
    for p in PRs:
        pr_info.append({'user': p['head']['user']['login'], 'title': p['title'],
                        'branch': p['head']['ref'], 'url': p['html_url']})

    with open(pr_list_file, 'w') as f:
        json.dump(pr_info, f)


if __name__ == "__main__":
    update_papers()
