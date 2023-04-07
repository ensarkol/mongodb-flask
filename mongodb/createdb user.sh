#!/bin/bash

mongo <<EOF
use stajdb
db.createUser(
   {
     user: "stajuser",
     pwd: "stajpassword",
     roles: [ { role: "readWrite", db: "stajdb" } ]
   }
)
EOF
