SELECT *
FROM {{ source('stock_information', 'stock_information') }}
