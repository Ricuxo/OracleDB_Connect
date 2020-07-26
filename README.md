Uma classe para conexão com o banco de dados Oracle utiliando cx_Oracle.

### Dependências

* cx_Oracle 
* Oracle client instalado
* Caminho do Oracle Client configurado: PATH (windows) ou LD_LIBRARY_PATH (Linux)

### Exemplo de utilização

```python
from conn_db import OracleDB

bduser = 'teste_henrique'
bdpass = 'oracle'
host = '192.168.0.150'
port = 1521
sid =  'ORCL'
sql_command = "select object_name,object_type from user_objects"

db = OracleDB(bduser, bdpass, host, port, sid)
query_results = db.execute_sql_command(host, sid, sql_command)
for query_result in query_results:
    print(query_result)
```

### Exemplo da saída

```python
python .\test.py
('T1', 'TABLE')
```

### Saída executando a query no banco de dados

```sql
[oracle@oracle ~]$ sqlplus teste_henrique/oracle

SQL*Plus: Release 12.2.0.1.0 Production on Sun Jul 26 16:10:35 2020

Copyright (c) 1982, 2016, Oracle.  All rights reserved.

Last Successful login time: Sun Jul 26 2020 16:10:11 -03:00

Connected to:
Oracle Database 12c Enterprise Edition Release 12.2.0.1.0 - 64bit Production

SQL> col object_name for a30
SQL> select object_name,object_type from user_objects;

OBJECT_NAME                    OBJECT_TYPE
------------------------------ -----------------------
T1                             TABLE
```

### Observação

* Todas as variáveis devem ser alteradas.
* Enviar comando com o usuário sys precisa alterar a conexão do cx_Oracle, pois precisa do parâmetro "as sysdba"

Para mais exemplos acesse: http://hsslab.com.br/

