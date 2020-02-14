# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: sqlite3.dump


def _iterdump(connection):
    cu = connection.cursor()
    yield 'BEGIN TRANSACTION;'
    q = '\n        SELECT "name", "type", "sql"\n        FROM "sqlite_master"\n            WHERE "sql" NOT NULL AND\n            "type" == \'table\'\n            ORDER BY "name"\n        '
    schema_res = cu.execute(q)
    for table_name, type, sql in schema_res.fetchall():
        if table_name == 'sqlite_sequence':
            yield 'DELETE FROM "sqlite_sequence";'
        else:
            if table_name == 'sqlite_stat1':
                yield 'ANALYZE "sqlite_master";'
            else:
                if table_name.startswith('sqlite_'):
                    continue
                else:
                    yield '%s;' % sql
        table_name_ident = table_name.replace('"', '""')
        res = cu.execute(('PRAGMA table_info("{0}")').format(table_name_ident))
        column_names = [ str(table_info[1]) for table_info in res.fetchall() ]
        q = ('SELECT \'INSERT INTO "{0}" VALUES({1})\' FROM "{0}";').format(table_name_ident, (',').join((('\'||quote("{0}")||\'').format(col.replace('"', '""')) for col in column_names)))
        query_res = cu.execute(q)
        for row in query_res:
            yield '%s;' % row[0]

    q = '\n        SELECT "name", "type", "sql"\n        FROM "sqlite_master"\n            WHERE "sql" NOT NULL AND\n            "type" IN (\'index\', \'trigger\', \'view\')\n        '
    schema_res = cu.execute(q)
    for name, type, sql in schema_res.fetchall():
        yield '%s;' % sql

    yield 'COMMIT;'