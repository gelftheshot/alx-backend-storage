-- createing index from only the first letter of column
CREATE INDEX idx_name_first_score
ON name ( name(1), score );
